[app]
title = Face Recognition App
package.name = faceapp
package.domain = org.apurv
source.dir = .
source.include_exts = py,png,jpg,kv,mp3
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
# To support camera and sound playback
android.hardware = camera, camera.autofocus

[buildozer]
log_level = 2
warn_on_root = 1
