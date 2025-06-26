import os
import cv2
import numpy as np
import threading
import time
import requests
from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

KNOWN_FACES_DIR = "known_faces"
RECOGNITION_INTERVAL = 600
AUDIO_FILE = "thank_you.mp3"
GOOGLE_FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScO9FVgTOXCeuw210SK6qx2fXiouDqouy7TTuoI6UD80ZpYvQ/formResponse"
FORM_FIELDS = {
    "name": "entry.935510406",
    "emp_id": "entry.886652582",
    "date": "entry.1160275796",
    "time": "entry.32017675",
}

def get_camera():
    for cam_id in (0, 1):
        cap = cv2.VideoCapture(cam_id)
        if cap.isOpened():
            print(f"[INFO] Using camera {cam_id}")
            return cap
        cap.release()
    raise RuntimeError("No working camera found (IDs 0 or 1).")

class FaceApp(App):
    def build(self):
        try:
            self.capture = get_camera()
        except RuntimeError as exc:
            Popup(title="Camera Error", content=Label(text=str(exc)), size_hint=(0.8, 0.3)).open()
            raise

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.recognizer, self.label_map = self.train_recognizer()
        self.last_seen_time = {}

        layout = BoxLayout(orientation="vertical")
        self.image = Image()
        self.button = Button(text="Register New Face", size_hint=(1, 0.1))
        self.button.bind(on_press=self.register_popup)

        layout.add_widget(self.image)
        layout.add_widget(self.button)

        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if not ret:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if self.recognizer:
            for (x, y, w, h) in faces:
                roi = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
                label_id, confidence = self.recognizer.predict(roi)

                if confidence < 70 and label_id in self.label_map:
                    label = self.label_map[label_id]
                    name, emp_id = label.split("_")
                    now = time.time()

                    if label_id not in self.last_seen_time or now - self.last_seen_time[label_id] > RECOGNITION_INTERVAL:
                        threading.Thread(target=self.play_sound_and_submit, args=(name, emp_id), daemon=True).start()
                        self.last_seen_time[label_id] = now

                    cv2.putText(frame, name.capitalize(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        buf = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
        self.image.texture = texture

    def train_recognizer(self):
        faces, labels = [], []
        label_map = {}
        if not os.path.exists(KNOWN_FACES_DIR):
            os.makedirs(KNOWN_FACES_DIR)

        for file in os.listdir(KNOWN_FACES_DIR):
            if file.lower().endswith((".jpg", ".png")):
                try:
                    name, emp_id, _ = file.split("_", 2)
                except ValueError:
                    continue
                label = f"{name}_{emp_id}"
                img = cv2.imread(os.path.join(KNOWN_FACES_DIR, file), cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue
                img = cv2.resize(img, (200, 200))
                if label not in label_map.values():
                    label_map[len(label_map)] = label
                faces.append(img)
                labels.append(list(label_map.values()).index(label))

        if len(faces) < 2:
            return None, None

        if not hasattr(cv2, "face"):
            raise ImportError("cv2.face module not found – install opencv-contrib-python.")

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(labels))
        return recognizer, label_map

    def register_popup(self, _instance):
        box = BoxLayout(orientation="vertical", spacing=8, padding=10)
        name_in = TextInput(hint_text="Full name", multiline=False)
        id_in = TextInput(hint_text="Employee ID", multiline=False)
        btn = Button(text="Capture Faces", size_hint=(1, 0.3))

        box.add_widget(Label(text="Enter details:", size_hint=(1, 0.2)))
        box.add_widget(name_in)
        box.add_widget(id_in)
        box.add_widget(btn)

        pop = Popup(title="Register Face", content=box, size_hint=(0.9, 0.6))

        def submit(_):
            name = name_in.text.strip().lower()
            emp_id = id_in.text.strip().upper()
            pop.dismiss()
            if name and emp_id:
                threading.Thread(target=self.register_new_face, args=(name, emp_id), daemon=True).start()

        btn.bind(on_press=submit)
        pop.open()

    def register_new_face(self, name, emp_id):
        saved = 0
        for seq in range(1, 11):
            ret, frame = self.capture.read()
            if not ret:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                face = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
                cv2.imwrite(os.path.join(KNOWN_FACES_DIR, f"{name}_{emp_id}_{seq}.jpg"), face)
                saved += 1
                break
            time.sleep(0.25)

        print(f"[INFO] Saved {saved} images for {name} ({emp_id}).")
        self.recognizer, self.label_map = self.train_recognizer()

    def play_sound_and_submit(self, name, emp_id):
        snd = SoundLoader.load(AUDIO_FILE)
        if snd:
            snd.play()
        self.send_to_google_form(name, emp_id)

    def send_to_google_form(self, name, emp_id):
        now = datetime.now()
        data = {
            FORM_FIELDS["name"]: name,
            FORM_FIELDS["emp_id"]: emp_id,
            FORM_FIELDS["date"]: now.strftime("%Y-%m-%d"),
            FORM_FIELDS["time"]: now.strftime("%H:%M:%S"),
        }
        try:
            requests.post(GOOGLE_FORM_URL, data=data, timeout=5)
            print(f"[INFO] Attendance submitted for {name} ({emp_id})")
        except requests.RequestException as err:
            print(f"[ERROR] Submission failed: {err}")

if __name__ == "__main__":
    FaceApp().run()
