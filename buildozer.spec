[app]
title = FaceApp
package.name = faceapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0
requirements = python3,kivy,opencv-contrib-python,numpy,pillow,requests
orientation = portrait
fullscreen = 1

# Icons
icon.filename = %(source.dir)s/icon.png

# Supported orientation (one of landscape, portrait, all, sensor)
orientation = portrait

# Android permissions
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECORD_AUDIO

# Android features
android.features = android.hardware.camera, android.hardware.camera.autofocus

# Entry point of your application
entrypoint = main.py

# Package format for Android
android.archs = armeabi-v7a, arm64-v8a
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 24
android.gradle_dependencies = androidx.exifinterface:exifinterface:1.3.3

# Include .mp3 file
include_patterns = assets/*,*.mp3

# Hide status bar
android.hide_statusbar = 1

# Ensure logcat output on crashes
log_level = 2

# Disable automatic internet check
android.disable_internet_state_permission = False

# To speed up builds
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# Fix some OpenCV issues on certain phones
android.useandroidx = True

# Skip requirements check (useful for contrib modules)
ignore_setup_py = 1

# Save build outputs
copy_libs = 1

# To avoid OpenCV crash with camera usage
android.add_jars = libs/

# Allow external mp3 to load
android.allow_backup = True
android.extra_permissions = android.permission.FOREGROUND_SERVICE

# Keep old apk
android.keep_build_dir = True
