

''' from ComputerVision.m file ''' 
# starting from line 413
# ending on line 621

    case 2 % Running buoy detection
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
        found = false;
        
        lowerb = colorthresh(1,1,:);    % lower bound
        upperb = colorthresh(1,2,:);    % upper bound
        
        %% Camera initialization
        
        switch camdevice
            case 'webcam'
                img = camera.read();
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
                img = img(150:480,163:652,:);
        end
        
        l = size(img,1); % length
        w = size(img,2); % width
        %%
        origin = [l/2,w/2];             % Sets the origin coordinates
        
        %% while loop
        cviMsg.CameraNumber = 1;
        while cviMsg.CameraNumber == 1
            
            %% Processing
            img = imrotate(img,180);
            blur = imresize(cv.medianBlur(img,'KSize',5),1/scale); % blur color image
            HSV = rgb2hsv(blur);        % convert color image to LAB colorspace
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
            A = zeros(numcnts,2);false
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
                            fcdMsg.FrontCamVerticalDistance = delta_h;
                            delta_x = (center(1)-origin(1));
                            fcdMsg.FrontCamHorizontalDistance = delta_x;
                            distance = given_distance*given_radius/radius;
                            fcdMsg.FrontCamForwardDistance = distance;
                            found = true;
                            distance = double(distance);
                            delta_x = double(distance);
                            fprintf('Height:%3.2f Angle:%3.2f Distance:%3.2f\n',delta_h,delta_x,distance); % print the calculated height and amount needed to turn
                        end
                        k = k+1;
                    end
                end
            else
                fcdMsg.FrontCamVerticalDistance = 999;
                fcdMsg.FrontCamHorizontalDistance = 999;
                fcdMsg.FrontCamForwardDistance = 999;
                fprintf('OBJECT LOST\n');
            end
            if videofeed
                img = cv.putText(img,sprintf('GAIN = %d EXPOSURE = %d',g1,e1),...
        [10,20],'FontFace','HersheyPlain','Color',[0,255,0]);
                imshow(imresize(img,1/display));
            end
            switch camdevice
                case 'webcam'
                    img = camera.read(); % initialize camera image for next loop
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
%                             start(camera);
                            img = getsnapshot(camera);
%                             stop(camera);
                            
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
                    img = img(150:480,161:650,:);
            end
            
            if ~found
                fcdMsg.FrontCamVerticalDistance = 999;
                fcdMsg.FrontCamHorizontalDistance = 999;
                fcdMsg.FrontCamForwardDistance = 999;
                fprintf('OBJECT LOST\n');
            end
            
            send(fcdPub, fcdMsg);
            cviMsg = receive(cviSub) ;
            found = false;
        end
