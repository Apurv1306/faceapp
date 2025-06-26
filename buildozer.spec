[app]
title = FaceApp
package.name = faceapp
package.domain = org.faceapp
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,mp3
version = 1.0

# Core dependencies
requirements = python3,kivy,opencv,ffpyplayer,numpy,requests,pillow

orientation = portrait
fullscreen = 1

# Android permissions (runtime requested in code)
android.permissions = CAMERA,INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Support both 32- and 64-bit
android.archs = armeabi-v7a,arm64-v8a

# Use latest Android platform to support camera + OpenCV
android.api = 34
android.minapi = 28

# Use compatible NDK
android.ndk = 25b
android.accept_sdk_license = True

# Include OpenCV contrib for cv2.face
p4a.extra_args = --recipe opencv --opencv-include-contrib

# Bundle native libraries with APK to avoid missing .so errors
android.copy_libs = 1
android.allow_backup = False

# Build output verbosity
log_level = 2
warn_on_root = 1
