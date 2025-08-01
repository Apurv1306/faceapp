[app]
title = FaceApp
package.name = faceapp
package.domain = org.yourdomain
source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0

requirements = python3,kivy,opencv-python,requests,pandas,fpdf,plyer,edge-tts,pygame,apscheduler
android.permissions = CAMERA, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

orientation = portrait
icon.filename = %(source.dir)s/data/icon.png

android.minapi = 21
android.api = 31
android.sdk = 31
android.ndk = 23b
android.private_storage = False
