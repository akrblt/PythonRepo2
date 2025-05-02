import cv2
import numpy as np
import mediapipe as mp
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk
import threading

# Mediapipe face mesh setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Global variables
overlay_image = None
cap = None
running = False

def select_image():
    global overlay_image
    path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if path:
        overlay_image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

def add_overlay(frame, landmarks, overlay_img):
    try:
        left_eye = landmarks[33]   # Left eye outer
        right_eye = landmarks[263] # Right eye outer
        nose = landmarks[1]        # Nose tip

        face_width = int(np.linalg.norm(np.array(right_eye) - np.array(left_eye)) * 2)

        center_x = int(nose[0])
        center_y = int(nose[1])
        x = int(center_x - face_width / 2)
        y = int(center_y - face_width / 2)

        resized_overlay = cv2.resize(overlay_img, (face_width, face_width))

        for i in range(resized_overlay.shape[0]):
            for j in range(resized_overlay.shape[1]):
                if resized_overlay[i, j, 3] != 0:  # alpha channel
                    if 0 <= y+i < frame.shape[0] and 0 <= x+j < frame.shape[1]:
                        frame[y+i, x+j] = resized_overlay[i, j, :3]
    except:
        pass
    return frame

def start_camera():
    global cap, running
    if overlay_image is None:
        print("Please select a face image first.")
        return
    running = True
    cap = cv2.VideoCapture(0)
    thread = threading.Thread(target=video_loop)
    thread.start()

def stop_camera():
    global running
    running = False

def video_loop():
    global cap, running
    while running:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                landmarks = []
                h, w, _ = frame.shape
                for lm in face_landmarks.landmark:
                    x, y = int(lm.x * w), int(lm.y * h)
                    landmarks.append((x, y))
                frame = add_overlay(frame, landmarks, overlay_image)

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    cap.release()

# Tkinter GUI
app = Tk()
app.title("Fake Face - Mediapipe Version")
app.geometry("800x600")

btn_select = Button(app, text="Select Face (PNG)", command=select_image)
btn_select.pack()

btn_start = Button(app, text="Start Camera", command=start_camera)
btn_start.pack()

btn_stop = Button(app, text="Stop Camera", command=stop_camera)
btn_stop.pack()

video_label = Label(app)
video_label.pack()

app.mainloop()
