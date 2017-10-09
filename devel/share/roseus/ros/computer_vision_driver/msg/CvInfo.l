;; Auto-generated. Do not edit!


(when (boundp 'computer_vision_driver::CvInfo)
  (if (not (find-package "COMPUTER_VISION_DRIVER"))
    (make-package "COMPUTER_VISION_DRIVER"))
  (shadow 'CvInfo (find-package "COMPUTER_VISION_DRIVER")))
(unless (find-package "COMPUTER_VISION_DRIVER::CVINFO")
  (make-package "COMPUTER_VISION_DRIVER::CVINFO"))

(in-package "ROS")
;;//! \htmlinclude CvInfo.msg.html


(defclass computer_vision_driver::CvInfo
  :super ros::object
  :slots (_cameraNumber _taskNumber _givenColor _givenShape _givenLength _givenDistance ))

(defmethod computer_vision_driver::CvInfo
  (:init
   (&key
    ((:cameraNumber __cameraNumber) 0)
    ((:taskNumber __taskNumber) 0)
    ((:givenColor __givenColor) 0)
    ((:givenShape __givenShape) 0)
    ((:givenLength __givenLength) 0.0)
    ((:givenDistance __givenDistance) 0.0)
    )
   (send-super :init)
   (setq _cameraNumber (round __cameraNumber))
   (setq _taskNumber (round __taskNumber))
   (setq _givenColor (round __givenColor))
   (setq _givenShape (round __givenShape))
   (setq _givenLength (float __givenLength))
   (setq _givenDistance (float __givenDistance))
   self)
  (:cameraNumber
   (&optional __cameraNumber)
   (if __cameraNumber (setq _cameraNumber __cameraNumber)) _cameraNumber)
  (:taskNumber
   (&optional __taskNumber)
   (if __taskNumber (setq _taskNumber __taskNumber)) _taskNumber)
  (:givenColor
   (&optional __givenColor)
   (if __givenColor (setq _givenColor __givenColor)) _givenColor)
  (:givenShape
   (&optional __givenShape)
   (if __givenShape (setq _givenShape __givenShape)) _givenShape)
  (:givenLength
   (&optional __givenLength)
   (if __givenLength (setq _givenLength __givenLength)) _givenLength)
  (:givenDistance
   (&optional __givenDistance)
   (if __givenDistance (setq _givenDistance __givenDistance)) _givenDistance)
  (:serialization-length
   ()
   (+
    ;; int32 _cameraNumber
    4
    ;; int32 _taskNumber
    4
    ;; int32 _givenColor
    4
    ;; int32 _givenShape
    4
    ;; float32 _givenLength
    4
    ;; float32 _givenDistance
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _cameraNumber
       (write-long _cameraNumber s)
     ;; int32 _taskNumber
       (write-long _taskNumber s)
     ;; int32 _givenColor
       (write-long _givenColor s)
     ;; int32 _givenShape
       (write-long _givenShape s)
     ;; float32 _givenLength
       (sys::poke _givenLength (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _givenDistance
       (sys::poke _givenDistance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _cameraNumber
     (setq _cameraNumber (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _taskNumber
     (setq _taskNumber (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _givenColor
     (setq _givenColor (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _givenShape
     (setq _givenShape (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _givenLength
     (setq _givenLength (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _givenDistance
     (setq _givenDistance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get computer_vision_driver::CvInfo :md5sum-) "8723a30b7f69c63ec944a866a7c37339")
(setf (get computer_vision_driver::CvInfo :datatype-) "computer_vision_driver/CvInfo")
(setf (get computer_vision_driver::CvInfo :definition-)
      "int32 cameraNumber
int32 taskNumber
int32 givenColor
int32 givenShape
float32 givenLength
float32 givenDistance

")



(provide :computer_vision_driver/CvInfo "8723a30b7f69c63ec944a866a7c37339")


