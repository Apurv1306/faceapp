[app]
title = FaceApp
package.name = faceapp
package.domain = org.faceapp
source.dir = .
source.include_exts = py,png,jpg,kv,mp3
version = 1.0
requirements = python3,kivy,opencv-contrib-python,numpy,pillow,requests
orientation = portrait
fullscreen = 1

android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO
android.archs = armeabi-v7a,arm64-v8a
android.api = 34
android.minapi = 28
android.ndk = 26b
android.accept_sdk_license = True
log_level = 2
android.allow_backup = False
android.copy_libs = 1

# If packaged via Docker, no need for sdk paths; else:
# android.sdk_path = /path/to/android/sdk
# android.ndk_path = /path/to/android/ndk

