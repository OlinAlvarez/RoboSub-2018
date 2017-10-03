
(cl:in-package :asdf)

(defsystem "computer_vision_driver-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CvInfo" :depends-on ("_package_CvInfo"))
    (:file "_package_CvInfo" :depends-on ("_package"))
  ))