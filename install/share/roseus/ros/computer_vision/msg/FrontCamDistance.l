;; Auto-generated. Do not edit!


(when (boundp 'computer_vision::FrontCamDistance)
  (if (not (find-package "COMPUTER_VISION"))
    (make-package "COMPUTER_VISION"))
  (shadow 'FrontCamDistance (find-package "COMPUTER_VISION")))
(unless (find-package "COMPUTER_VISION::FRONTCAMDISTANCE")
  (make-package "COMPUTER_VISION::FRONTCAMDISTANCE"))

(in-package "ROS")
;;//! \htmlinclude FrontCamDistance.msg.html


(defclass computer_vision::FrontCamDistance
  :super ros::object
  :slots (_frontCamForwardDistance _frontCamHorizontalDistance _frontCamVerticalDistance ))

(defmethod computer_vision::FrontCamDistance
  (:init
   (&key
    ((:frontCamForwardDistance __frontCamForwardDistance) 0.0)
    ((:frontCamHorizontalDistance __frontCamHorizontalDistance) 0.0)
    ((:frontCamVerticalDistance __frontCamVerticalDistance) 0.0)
    )
   (send-super :init)
   (setq _frontCamForwardDistance (float __frontCamForwardDistance))
   (setq _frontCamHorizontalDistance (float __frontCamHorizontalDistance))
   (setq _frontCamVerticalDistance (float __frontCamVerticalDistance))
   self)
  (:frontCamForwardDistance
   (&optional __frontCamForwardDistance)
   (if __frontCamForwardDistance (setq _frontCamForwardDistance __frontCamForwardDistance)) _frontCamForwardDistance)
  (:frontCamHorizontalDistance
   (&optional __frontCamHorizontalDistance)
   (if __frontCamHorizontalDistance (setq _frontCamHorizontalDistance __frontCamHorizontalDistance)) _frontCamHorizontalDistance)
  (:frontCamVerticalDistance
   (&optional __frontCamVerticalDistance)
   (if __frontCamVerticalDistance (setq _frontCamVerticalDistance __frontCamVerticalDistance)) _frontCamVerticalDistance)
  (:serialization-length
   ()
   (+
    ;; float32 _frontCamForwardDistance
    4
    ;; float32 _frontCamHorizontalDistance
    4
    ;; float32 _frontCamVerticalDistance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _frontCamForwardDistance
       (sys::poke _frontCamForwardDistance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _frontCamHorizontalDistance
       (sys::poke _frontCamHorizontalDistance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _frontCamVerticalDistance
       (sys::poke _frontCamVerticalDistance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _frontCamForwardDistance
     (setq _frontCamForwardDistance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _frontCamHorizontalDistance
     (setq _frontCamHorizontalDistance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _frontCamVerticalDistance
     (setq _frontCamVerticalDistance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get computer_vision::FrontCamDistance :md5sum-) "65f5794fdf87a86db880b10f7ba78110")
(setf (get computer_vision::FrontCamDistance :datatype-) "computer_vision/FrontCamDistance")
(setf (get computer_vision::FrontCamDistance :definition-)
      "float32 frontCamForwardDistance
float32 frontCamHorizontalDistance
float32 frontCamVerticalDistance

")



(provide :computer_vision/FrontCamDistance "65f5794fdf87a86db880b10f7ba78110")


