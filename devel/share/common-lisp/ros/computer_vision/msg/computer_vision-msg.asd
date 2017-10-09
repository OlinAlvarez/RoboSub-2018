
(cl:in-package :asdf)

(defsystem "computer_vision-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FrontCamDistance" :depends-on ("_package_FrontCamDistance"))
    (:file "_package_FrontCamDistance" :depends-on ("_package"))
  ))