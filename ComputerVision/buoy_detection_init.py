
''' from ComputerVision.m file ''' 
# starting on line 180
# ending on line 407

%% Tasks
switch msg.TaskNumber
    case 1      % Initialize Buoy detection
        %% Initialize Color
        color = uint8([]);
        color(1,1,:) = colors_list{color_choice,2}; % pick color from RGB choices
        colorHSV = rgb2hsv(color);      % convert color choice to LAB colorspace
        color = colorHSV;
        huethresh = thresh_list{color_choice}(1);
        satthresh = thresh_list{color_choice}(2);
        huethresh = huethresh/255;
        satthresh = satthresh/255;
        colorthresh = zeros(1,2,2);
        colorthresh(:,:,1) = [color(:,:,1)-huethresh,color(:,:,1)+huethresh];
        colorthresh(:,:,2) = [color(:,:,2)-satthresh,color(:,:,2)+satthresh];
        colorthresh(:,:,1) = mod(colorthresh(:,:,1),1);
        colorthresh = uint8(colorthresh*255);
        
        
        
        lowerb = colorthresh(1,1,:);    % lower bound
        upperb = colorthresh(1,2,:);    % upper bound
        
        %% Camera initialization
        
        switch camdevice
            case 'webcam'
                %img = camera.read();
                img = snapshot(camera);
            case 'image'
                img = which('buoy.png');
                img = cv.imread(img, 'Flags',1);
            otherwise
%                 start(camera);
                img = getsnapshot(camera);
%                 stop(camera);
                hsvi = rgb2hsv(img);
                i = mean(mean(hsvi(:,:,3)));
                if i < threshL
                    while i < threshL
                        e1 = e1 + 1;
                        exposure = sprintf('v4l2-ctl -d /dev/video0 -c exposure_absolute=%d',e1);
                        system(exposure);
%                         start(camera);
                        img = getsnapshot(camera);
%                         stop(camera);
                        
                        hsvi = rgb2hsv(img);
                        i = mean(mean(hsvi(:,:,3)));
                    end
                elseif i > threshH
                    while i > threshH
                        e1 = e1 - 1;
                        exposure = sprintf('v4l2-ctl -d /dev/video0 -c exposure_absolute=%d',e1);
                        system(exposure);
%                         start(camera);
                        img = getsnapshot(camera);
%                         stop(camera);
                        hsvi = rgb2hsv(img);
                        i = mean(mean(hsvi(:,:,3)));
                    end
                end
                %                 img = snapshot(camera);
                img = img(150:480,163:652,:);
        end
        
        l = size(img,1); % length
        w = size(img,2); % width
        %%
        origin = [l/2,w/2];             % Sets the origin coordinates
        
        
        %%%while ~found || strcmp(msgReceiveFromMaster,'keepFinding')
        m = 1;  % total attempts
        n = 1;  % successful attempts
        while m < 60 && n < 30 && (60-m > 30-n) % take at most 60 frames
            %% Processing
            img = imrotate(img,180);
            blur = imresize(cv.medianBlur(img,'KSize',5),1/scale); % blur color image
            HSV = rgb2hsv(blur);        % convert color image to HSV colorspace
            HSV = uint8(HSV*255);
            
            
            %% Color Threshold - filter out all unwanted color
            if lowerb(:,:,1) > upperb(:,:,1)
                mask = (HSV(:,:,2) > lowerb(:,:,2)) &...
                    (HSV(:,:,2) < upperb(:,:,2)) & ((HSV(:,:,1) > lowerb(:,:,1))...
                    | (HSV(:,:,1) < upperb(:,:,1))); % does the same thing as cv.inRange()
            else
                mask = (HSV(:,:,2) > lowerb(:,:,2)) &...
                    (HSV(:,:,2) < upperb(:,:,2)) & (HSV(:,:,1) > lowerb(:,:,1))...
                    & (HSV(:,:,1) < upperb(:,:,1));
            end
            
            
            
            cnts = cv.findContours(mask,'Mode','External','Method','Simple'); % detect all contours
            
            %% Arrange contours from largest to smallest
            numcnts = numel(cnts);
            A = zeros(numcnts,2);
            circles = false;
            if numcnts > 0
                A(1:numcnts,2) = (1:numcnts);
                for i = 1:numcnts
                    A(i,1) = cv.contourArea(cnts{i});
                end
                A = sortrows(A,'descend');
                k = 1;
                
                
                if ~isnan(A(1,2))
                    %% Calculate the shape of the detected contour
                    while ~circles && k < 10 && k <= length(A(:,1)) && A(k,1) > 2
                        c = A(k,2);             % index of contour with largest area
                        cnt = cnts{c};
                        M = cv.moments(cnt);
                        cX = int16(M.m10/M.m00);
                        cY = int16(M.m01/M.m00);
                        peri = cv.arcLength(cnt,'Closed',1);
                        approx = cv.approxPolyDP(cnt,'Epsilon',...
                            0.04*peri,'Closed',1); % approximate the corners of the shape
                        if length(approx) > 3
                            circles = true;
                            n = n + 1;
                            [~,radius] =  cv.minEnclosingCircle(cnt);
                            if videofeed
                                if corners
                                    for i = 1:length(approx)
                                        img = cv.circle(img,scale*approx{i},3,'Color',[0,0,255],...
                                            'Thickness',-1); % draws corners of shape
                                    end
                                end
                                
                                img = cv.circle(img,scale.*[cX,cY],7,'Color',[255,255,255],...
                                    'Thickness',-1); % draws center of shape
                                
                                img = cv.circle(img,scale.*[cX,cY], scale.*radius, 'Color',[0,0,255], ...
                                    'Thickness',2, 'LineType','AA'); % draw the circle outline
                            end
                            center = scale.*[cX,cY];
                            radius = scale.*radius;
                            delta_h = (origin(2)-center(2));
                            meandelta_h(n) = delta_h;
                            %                             fcdMsg.FrontCamVerticalDistance = delta_h;
                            delta_x = (center(1)-origin(1));
                            meandelta_x(n) = delta_x;
                            %                             fcdMsg.FrontCamHorizontalDistance = delta_x;
                            distance = given_distance*given_radius/radius;
                            meandistance(n) = distance;
                            %                             fcdMsg.FrontCamForwardDistance = distance;
                            distance = double(distance);
                            %                             delta_x = (origin(1) - center(1))./10;
                            meantheta(n) = atand(double(distance/delta_x));
                            fprintf('Vertical:%3.2f Angle:%3.2f Distance:%3.2f\n',delta_h,meantheta(n),distance); % print the calculated height and amount needed to turn
                        end
                        k = k+1;
                    end
                end
            end
            
            
            if videofeed
                img = cv.putText(img,sprintf('GAIN = %d EXPOSURE = %d',g1,e1),...
        [10,20],'FontFace','HersheyPlain','Color',[0,255,0]);
                imshow(imresize(img,1/display));
            end
            switch camdevice
                case 'webcam'
                    %img = camera.read();        % initialize camera image for next loop
                    img = snapshot(camera);
                case 'image'
                    break
                otherwise
%                     start(camera);
                    img = getsnapshot(camera);
%                     stop(camera);
                    hsvi = rgb2hsv(img);
                    i = mean(mean(hsvi(:,:,3)));
                    if i < threshL
                        while i < threshL
                            e1 = e1 + 1;
                            exposure = sprintf('v4l2-ctl -d /dev/video0 -c exposure_absolute=%d',e1);
                            system(exposure);
                            start(camera);
                            img = getsnapshot(camera);
                            stop(camera);
                            
                            hsvi = rgb2hsv(img);
                            i = mean(mean(hsvi(:,:,3)));
                        end
                    elseif i > threshH
                        while i > threshH
                            e1 = e1 - 1;
                            exposure = sprintf('v4l2-ctl -d /dev/video0 -c exposure_absolute=%d',e1);
                            system(exposure);
                            start(camera);
                            img = getsnapshot(camera);
                            stop(camera);
                            hsvi = rgb2hsv(img);
                            i = mean(mean(hsvi(:,:,3)));
                        end
                    end
                    img = img(1:480,163:652,:);
            end
            m = m + 1;
        end
        if n == 30 || found
            if ~found
                found = true;
            end
            tiMsg.State = 1;
            tiMsg.Angle = mean(meantheta(15:end));
            tiMsg.Height = mean(meandelta_h(15:end));
            
            %             send(fcdPub, fcdMsg);
            %     send(bcdPub, bcdMsg);
            %%%send(tiPub, tiMsg);
            
            %fcdMsg.FrontCamHorizontalDistance = mean(theta(15:end));
            %fcdMsg.FrontCamForwardDistance = mean(meandistance(15:end));
            fprintf('FOUND\nAVERAGE: Angle:%3.2f Height:%3.2f\n',tiMsg.Angle,tiMsg.Height);
            
        else
            tiMsg.State = 0;
            %imshow(img);
            %%%send(tiPub, tiMsg);
            fprintf('Finding...\n')
        end
        %%%end
