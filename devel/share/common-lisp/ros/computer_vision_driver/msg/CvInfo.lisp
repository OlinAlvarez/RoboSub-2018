; Auto-generated. Do not edit!


(cl:in-package computer_vision_driver-msg)


;//! \htmlinclude CvInfo.msg.html

(cl:defclass <CvInfo> (roslisp-msg-protocol:ros-message)
  ((cameraNumber
    :reader cameraNumber
    :initarg :cameraNumber
    :type cl:integer
    :initform 0)
   (taskNumber
    :reader taskNumber
    :initarg :taskNumber
    :type cl:integer
    :initform 0)
   (givenColor
    :reader givenColor
    :initarg :givenColor
    :type cl:integer
    :initform 0)
   (givenShape
    :reader givenShape
    :initarg :givenShape
    :type cl:integer
    :initform 0)
   (givenLength
    :reader givenLength
    :initarg :givenLength
    :type cl:float
    :initform 0.0)
   (givenDistance
    :reader givenDistance
    :initarg :givenDistance
    :type cl:float
    :initform 0.0))
)

(cl:defclass CvInfo (<CvInfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CvInfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CvInfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name computer_vision_driver-msg:<CvInfo> is deprecated: use computer_vision_driver-msg:CvInfo instead.")))

(cl:ensure-generic-function 'cameraNumber-val :lambda-list '(m))
(cl:defmethod cameraNumber-val ((m <CvInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision_driver-msg:cameraNumber-val is deprecated.  Use computer_vision_driver-msg:cameraNumber instead.")
  (cameraNumber m))

(cl:ensure-generic-function 'taskNumber-val :lambda-list '(m))
(cl:defmethod taskNumber-val ((m <CvInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision_driver-msg:taskNumber-val is deprecated.  Use computer_vision_driver-msg:taskNumber instead.")
  (taskNumber m))

(cl:ensure-generic-function 'givenColor-val :lambda-list '(m))
(cl:defmethod givenColor-val ((m <CvInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision_driver-msg:givenColor-val is deprecated.  Use computer_vision_driver-msg:givenColor instead.")
  (givenColor m))

(cl:ensure-generic-function 'givenShape-val :lambda-list '(m))
(cl:defmethod givenShape-val ((m <CvInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision_driver-msg:givenShape-val is deprecated.  Use computer_vision_driver-msg:givenShape instead.")
  (givenShape m))

(cl:ensure-generic-function 'givenLength-val :lambda-list '(m))
(cl:defmethod givenLength-val ((m <CvInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision_driver-msg:givenLength-val is deprecated.  Use computer_vision_driver-msg:givenLength instead.")
  (givenLength m))

(cl:ensure-generic-function 'givenDistance-val :lambda-list '(m))
(cl:defmethod givenDistance-val ((m <CvInfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader computer_vision_driver-msg:givenDistance-val is deprecated.  Use computer_vision_driver-msg:givenDistance instead.")
  (givenDistance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CvInfo>) ostream)
  "Serializes a message object of type '<CvInfo>"
  (cl:let* ((signed (cl:slot-value msg 'cameraNumber)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'taskNumber)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'givenColor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'givenShape)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'givenLength))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'givenDistance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CvInfo>) istream)
  "Deserializes a message object of type '<CvInfo>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cameraNumber) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'taskNumber) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'givenColor) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'givenShape) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'givenLength) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'givenDistance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CvInfo>)))
  "Returns string type for a message object of type '<CvInfo>"
  "computer_vision_driver/CvInfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CvInfo)))
  "Returns string type for a message object of type 'CvInfo"
  "computer_vision_driver/CvInfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CvInfo>)))
  "Returns md5sum for a message object of type '<CvInfo>"
  "8723a30b7f69c63ec944a866a7c37339")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CvInfo)))
  "Returns md5sum for a message object of type 'CvInfo"
  "8723a30b7f69c63ec944a866a7c37339")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CvInfo>)))
  "Returns full string definition for message of type '<CvInfo>"
  (cl:format cl:nil "int32 cameraNumber~%int32 taskNumber~%int32 givenColor~%int32 givenShape~%float32 givenLength~%float32 givenDistance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CvInfo)))
  "Returns full string definition for message of type 'CvInfo"
  (cl:format cl:nil "int32 cameraNumber~%int32 taskNumber~%int32 givenColor~%int32 givenShape~%float32 givenLength~%float32 givenDistance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CvInfo>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CvInfo>))
  "Converts a ROS message object to a list"
  (cl:list 'CvInfo
    (cl:cons ':cameraNumber (cameraNumber msg))
    (cl:cons ':taskNumber (taskNumber msg))
    (cl:cons ':givenColor (givenColor msg))
    (cl:cons ':givenShape (givenShape msg))
    (cl:cons ':givenLength (givenLength msg))
    (cl:cons ':givenDistance (givenDistance msg))
))
