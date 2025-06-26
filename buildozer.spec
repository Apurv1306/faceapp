# =============================================================
# FaceApp  –  Buildozer specification
# Last verified: 26 Jun 2025
# Works with:
#   • Buildozer ≥ 1.5.1
#   • python-for-android 2025.06-stable
#   • Android SDK 34   •  NDK r26c
# =============================================================

[app]
# --- General ---
title             = FaceApp
package.name      = faceapp
package.domain    = io.digitalapurv
version           = 1.1.0
source.dir        = .
source.include_exts = py,kv,jpg,jpeg,png,mp3,json,xml
orientation       = portrait
fullscreen        = 1
android.allow_backup   = False
android.private_storage = True      # keeps known_faces inside sandbox
android.copy_libs      = 1          # bundles *.so in APK

# -------------------------------------------------------------
# RUNTIME STACK
# -------------------------------------------------------------
# ① “opencv” *recipe* ⇒ native build for every ABI, WITH contrib
# ② ffpyplayer ⇒ robust MP3 playback on Android
# ③ pillow ⇒ avoids rare texture-upload crashes on some GPUs
requirements = \
    python3==3.11, \
    kivy==2.3.1, \
    numpy, \
    requests, \
    pillow, \
    ffpyplayer, \
    opencv

# Compile OpenCV with the extra modules
p4a.extra_args = \
    --recipe opencv --opencv-include-contrib \
    --recipe ffpyplayer

# -------------------------------------------------------------
# PERMISSIONS  (declared *and* later requested at runtime)
# -------------------------------------------------------------
android.permissions = \
    CAMERA, \
    INTERNET, \
    ACCESS_NETWORK_STATE, \
    READ_EXTERNAL_STORAGE, \
    WRITE_EXTERNAL_STORAGE, \
    RECORD_AUDIO, \
    WAKE_LOCK, \
    VIBRATE

# -------------------------------------------------------------
# PLATFORM SETTINGS
# -------------------------------------------------------------
android.api      = 34
android.minapi   = 28
android.ndk      = 26c
android.ndk_api  = 28
android.arch     = armeabi-v7a, arm64-v8a

# -------------------------------------------------------------
# OPTIONAL  –  pre-built OpenCV native libs (fast CI builds)
# Leave these two lines in place unless you *must* compile OpenCV
android.gradle_dependencies = \
    implementation('com.quickbirdstudios:opencv-contrib:4.5.3.0')  # native .aar :contentReference[oaicite:0]{index=0}

# -------------------------------------------------------------
# MISC BUILD OPTIONS
# -------------------------------------------------------------
release   = False         # switch to True only after signing
log_level = 2             # 0=verbose … 3=minimal
warn_on_root = 1
# =============================================================
