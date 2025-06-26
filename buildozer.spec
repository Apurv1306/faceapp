[app]
title = FaceApp
package.name = faceapp
package.domain = org.faceapp
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,mp3
version = 1.0

# Core dependencies
requirements = python3,kivy,ffi,pyjnius,numpy,requests,pillow,opencv

# OpenCV with face module + image-handling library for texture safety
# `opencv` here refers to the contrib recipe (see p4a.extra_args)
orientation = portrait
fullscreen = 1

# Permissions required at runtime
android.permissions = CAMERA,INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Supported ABIs
android.archs = armeabi-v7a,arm64-v8a

# Use latest Android platform
android.api = 34
android.minapi = 28

# Use a modern NDK with face module support
android.ndk = 25b
android.accept_sdk_license = True

# Use contrib modules to include cv2.face
p4a.extra_args = --recipe opencv --opencv-include-contrib

# Optimize package size and stability
android.copy_libs = 1
android.allow_backup = False

# Build verbosity
log_level = 2
warn_on_root = 1
