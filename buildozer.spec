[app]
title = FaceApp
package.name = faceapp
package.domain = org.digitalapurv
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0
requirements = python3,kivy,numpy,requests,opencv
orientation = portrait

android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 0