[app]
title = Attendance
package.name = faceapp
package.domain = org.faceapp
source.dir = .
source.include_exts = py,png,jpg,kv,mp3
version = 0.1
requirements = python3,kivy,opencv-python-headless,numpy,requests,pillow
orientation = portrait
fullscreen = 1

# Permissions
android.permissions = CAMERA,INTERNET,RECORD_AUDIO,WAKE_LOCK,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Presplash and Icon (optional)
# icon.filename = icon.png
# presplash.filename = splash.png

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 34
android.ndk = 26b
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True
android.archs = arm64-v8a

# Skip NDK install if using Docker
android.ndk_api = 34
