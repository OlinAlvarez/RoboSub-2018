; Auto-generated. Do not edit!


(cl:in-package computer_vision-msg)


;//! \htmlinclude FrontCamera.msg.html

(cl:defclass <FrontCamera> (roslisp-msg-protocol:ros-message)
  ((frontCamForwardDistance
    :reader frontCamForwardDistance
    :initarg :frontCamForwardDistance
    :type cl:float
    :initform 0.0)
   (frontCamHorizontalDistance
    :reader frontCamHorizontalDistance
    :initarg :frontCamHorizontalDistance
    :type cl:float
    :initform 0.0)
   (frontCamVerticalDistance
    :reader frontCamVerticalDistance
    :initarg :frontCamVerticalDistance
    :type cl:float
    :initform 0.0))
)

(cl:defclass FrontCamera (<FrontCamera>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FrontCamera>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FrontCamera)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name computer_vision-msg:<FrontCamera> is deprecated: use computer_vision-msg:FrontCamera instead.")))

(cl:ensure-generic-function 'frontCamForwardDistance-val :lambda-list '(m))
(cl:defmethod frontCamForwardDistance-val ((m <FrontCamera>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision-msg:frontCamForwardDistance-val is deprecated.  Use computer_vision-msg:frontCamForwardDistance instead.")
  (frontCamForwardDistance m))

(cl:ensure-generic-function 'frontCamHorizontalDistance-val :lambda-list '(m))
(cl:defmethod frontCamHorizontalDistance-val ((m <FrontCamera>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision-msg:frontCamHorizontalDistance-val is deprecated.  Use computer_vision-msg:frontCamHorizontalDistance instead.")
  (frontCamHorizontalDistance m))

(cl:ensure-generic-function 'frontCamVerticalDistance-val :lambda-list '(m))
(cl:defmethod frontCamVerticalDistance-val ((m <FrontCamera>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision-msg:frontCamVerticalDistance-val is deprecated.  Use computer_vision-msg:frontCamVerticalDistance instead.")
  (frontCamVerticalDistance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FrontCamera>) ostream)
  "Serializes a message object of type '<FrontCamera>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'frontCamForwardDistance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'frontCamHorizontalDistance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'frontCamVerticalDistance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FrontCamera>) istream)
  "Deserializes a message object of type '<FrontCamera>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'frontCamForwardDistance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'frontCamHorizontalDistance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'frontCamVerticalDistance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FrontCamera>)))
  "Returns string type for a message object of type '<FrontCamera>"
  "computer_vision/FrontCamera")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FrontCamera)))
  "Returns string type for a message object of type 'FrontCamera"
  "computer_vision/FrontCamera")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FrontCamera>)))
  "Returns md5sum for a message object of type '<FrontCamera>"
  "65f5794fdf87a86db880b10f7ba78110")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FrontCamera)))
  "Returns md5sum for a message object of type 'FrontCamera"
  "65f5794fdf87a86db880b10f7ba78110")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FrontCamera>)))
  "Returns full string definition for message of type '<FrontCamera>"
  (cl:format cl:nil "float32 frontCamForwardDistance~%float32 frontCamHorizontalDistance~%float32 frontCamVerticalDistance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FrontCamera)))
  "Returns full string definition for message of type 'FrontCamera"
  (cl:format cl:nil "float32 frontCamForwardDistance~%float32 frontCamHorizontalDistance~%float32 frontCamVerticalDistance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FrontCamera>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FrontCamera>))
  "Converts a ROS message object to a list"
  (cl:list 'FrontCamera
    (cl:cons ':frontCamForwardDistance (frontCamForwardDistance msg))
    (cl:cons ':frontCamHorizontalDistance (frontCamHorizontalDistance msg))
    (cl:cons ':frontCamVerticalDistance (frontCamVerticalDistance msg))
))
