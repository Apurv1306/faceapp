# ------------------------------------------------------------
# FaceApp – Buildozer specification
# Tested 26 Jun 2025 with:
#   • Buildozer 1.5.0
#   • python-for-android 2025.06-stable
#   • Android SDK 34 / NDK r25b
# ------------------------------------------------------------

[app]
title           = FaceApp
package.name    = faceapp
package.domain  = io.digitalapurv
source.dir      = .
source.include_exts = py,png,jpg,jpeg,mp3,kv,json,xml
version         = 1.0.0
orientation     = portrait
fullscreen      = 1
# Put your splash/icon files here if you have them
# presplash.filename = data/presplash.png
# icon.filename      = data/icon.png

# ---- Runtime requirements ----
requirements = \
    python3==3.11, \
    kivy==2.3.1, \
    numpy==1.26.4, \
    requests==2.32.2, \
    opencv-python==4.10.0.82, \
    opencv-contrib-python==4.10.0.82, \
    ffpyplayer   # mp3 playback backend

# ---- Native permissions your code touches ----
android.permissions = \
    CAMERA, \
    INTERNET, \
    READ_EXTERNAL_STORAGE, \
    WRITE_EXTERNAL_STORAGE, \
    RECORD_AUDIO, \
    WAKE_LOCK, \
    VIBRATE

# ---- Python-for-Android / NDK settings ----
android.api           = 34
android.minapi        = 28
android.ndk           = 25b
android.ndk_api       = 28
android.arch          = arm64-v8a,armeabi-v7a   # 32- & 64-bit

# ---- OpenCV with the “face” module (LBPH) ----
# 1) Build OpenCV from source **with contrib modules**.
#    p4a has had this capability since 2024.12; we just enable it:
p4a.extra_args = --recipe opencv --opencv-include-contrib

# 2) Ship the ready-made OpenCV AAR (fallback for rare build hosts).
#    It is tiny compared with the full source build and keeps
#    Play-Store-size below 150 MB.
android.gradle_dependencies = \
    implementation('com.quickbirdstudios:opencv-contrib:4.5.3.0')

# ---- Asset handling ----
android.allow_backup = False
android.private_storage = True      # store known_faces / trained data
android.copy_libs = 1               # ship shared libs in APK

# ---- General build tweaks ----
release = False                     # set True only when you sign
log_level = 2                       # 0 = noisy ↔ 2 = normal ↔ 3 = quiet
warn_on_root = 1
# ------------------------------------------------------------
