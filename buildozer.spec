[app]
title = Face Recognition
package.name = faceapp
package.domain = org.apurv.face
source.dir = .
source.include_exts = py,mp3,jpg,png
version = 1.0
requirements = python3,kivy,opencv-contrib-python,numpy,requests
orientation = portrait
fullscreen = 1
android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.arch = armeabi-v7a
android.hardware = camera, camera.autofocus

[buildozer]
log_level = 2
warn_on_root = 1
