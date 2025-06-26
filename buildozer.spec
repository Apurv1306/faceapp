# ============================================================
# FaceApp – Production-grade buildozer.spec
# Updated: 26 Jun 2025
# Tested with:
#   • Buildozer 1.5.1
#   • python-for-android 2025.06-stable
#   • Android SDK 34  |  NDK r26c
# ============================================================

[app]
title = FaceApp
package.name  = faceapp
package.domain = io.digitalapurv
source.dir = .
source.include_exts = py,kv,jpg,jpeg,png,mp3,json,xml
version = 1.1.0
orientation = portrait
fullscreen  = 1
android.allow_backup = False
android.private_storage = True        # stores known_faces safely
android.copy_libs = 1                 # bundles *.so in the APK

# ------------------------------------------------------------
# RUNTIME STACK
# ------------------------------------------------------------
# ① Use the **recipe** “opencv” instead of PyPI wheels – it is
#    compiled for every ABI and brings the cv2.face module. :contentReference[oaicite:0]{index=0}
# ② ffpyplayer = stable MP3 backend on Android.
# ③ pyjnius is pulled automatically; no need to list it.
requirements = \
    python3==3.11, \
    kivy==2.3.1, \
    numpy, \
    requests, \
    ffpyplayer, \
    opencv

# Build arguments for python-for-android
p4a.extra_args = \
    --recipe opencv --opencv-include-contrib \
    --recipe ffpyplayer

# ------------------------------------------------------------
# PERMISSIONS
# ------------------------------------------------------------
android.permissions = \
    CAMERA, \
    INTERNET, \
    ACCESS_NETWORK_STATE, \
    READ_EXTERNAL_STORAGE, \
    WRITE_EXTERNAL_STORAGE, \
    RECORD_AUDIO, \
    WAKE_LOCK, \
    VIBRATE

# API / ABI
android.api      = 34
android.minapi   = 28
android.ndk      = 26c
android.ndk_api  = 28
android.arch     = armeabi-v7a, arm64-v8a

# ------------------------------------------------------------
# OPTIONAL: ship OpenCV AAR instead of compiling (faster CI)
# Remove the next two lines if you prefer the full native build.
android.gradle_dependencies = \
    implementation('com.quickbirdstudios:opencv-contrib:4.5.3.0')   # native libs pre-built :contentReference[oaicite:1]{index=1}

# ------------------------------------------------------------
# MISC
# ------------------------------------------------------------
release   = False   # switch to True only for a signed Release/AAB
log_level = 2       # 0=very verbose … 3=quiet
warn_on_root = 1
# ============================================================
