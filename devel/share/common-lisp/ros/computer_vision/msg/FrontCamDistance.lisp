; Auto-generated. Do not edit!


(cl:in-package computer_vision-msg)


;//! \htmlinclude FrontCamDistance.msg.html

(cl:defclass <FrontCamDistance> (roslisp-msg-protocol:ros-message)
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

(cl:defclass FrontCamDistance (<FrontCamDistance>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FrontCamDistance>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FrontCamDistance)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name computer_vision-msg:<FrontCamDistance> is deprecated: use computer_vision-msg:FrontCamDistance instead.")))

(cl:ensure-generic-function 'frontCamForwardDistance-val :lambda-list '(m))
(cl:defmethod frontCamForwardDistance-val ((m <FrontCamDistance>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision-msg:frontCamForwardDistance-val is deprecated.  Use computer_vision-msg:frontCamForwardDistance instead.")
  (frontCamForwardDistance m))

(cl:ensure-generic-function 'frontCamHorizontalDistance-val :lambda-list '(m))
(cl:defmethod frontCamHorizontalDistance-val ((m <FrontCamDistance>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision-msg:frontCamHorizontalDistance-val is deprecated.  Use computer_vision-msg:frontCamHorizontalDistance instead.")
  (frontCamHorizontalDistance m))

(cl:ensure-generic-function 'frontCamVerticalDistance-val :lambda-list '(m))
(cl:defmethod frontCamVerticalDistance-val ((m <FrontCamDistance>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision-msg:frontCamVerticalDistance-val is deprecated.  Use computer_vision-msg:frontCamVerticalDistance instead.")
  (frontCamVerticalDistance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FrontCamDistance>) ostream)
  "Serializes a message object of type '<FrontCamDistance>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FrontCamDistance>) istream)
  "Deserializes a message object of type '<FrontCamDistance>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FrontCamDistance>)))
  "Returns string type for a message object of type '<FrontCamDistance>"
  "computer_vision/FrontCamDistance")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FrontCamDistance)))
  "Returns string type for a message object of type 'FrontCamDistance"
  "computer_vision/FrontCamDistance")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FrontCamDistance>)))
  "Returns md5sum for a message object of type '<FrontCamDistance>"
  "65f5794fdf87a86db880b10f7ba78110")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FrontCamDistance)))
  "Returns md5sum for a message object of type 'FrontCamDistance"
  "65f5794fdf87a86db880b10f7ba78110")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FrontCamDistance>)))
  "Returns full string definition for message of type '<FrontCamDistance>"
  (cl:format cl:nil "float32 frontCamForwardDistance~%float32 frontCamHorizontalDistance~%float32 frontCamVerticalDistance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FrontCamDistance)))
  "Returns full string definition for message of type 'FrontCamDistance"
  (cl:format cl:nil "float32 frontCamForwardDistance~%float32 frontCamHorizontalDistance~%float32 frontCamVerticalDistance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FrontCamDistance>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FrontCamDistance>))
  "Converts a ROS message object to a list"
  (cl:list 'FrontCamDistance
    (cl:cons ':frontCamForwardDistance (frontCamForwardDistance msg))
    (cl:cons ':frontCamHorizontalDistance (frontCamHorizontalDistance msg))
    (cl:cons ':frontCamVerticalDistance (frontCamVerticalDistance msg))
))
