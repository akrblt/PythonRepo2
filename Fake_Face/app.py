import cv2
import numpy as np
import mediapipe as mp
from tkinter import Tk, Button, Label, filedialog, OptionMenu, StringVar
from PIL import Image, ImageTk
import threading
import os
import datetime
import subprocess

# MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Global variables
overlay_image = None
overlay_images = {}
cap = None
running = False
camera_index = 0
latest_frame = None

# UI variables
face_var = StringVar()
camera_var = StringVar()

# Load face mask library
def load_face_library():
    global overlay_images
    face_dir = "face_masks"
    if not os.path.exists(face_dir):
        os.makedirs(face_dir)
    overlay_images = {}
    for filename in os.listdir(face_dir):
        if filename.endswith(".png"):
            path = os.path.join(face_dir, filename)
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            overlay_images[filename] = img
    if overlay_images:
        first = list(overlay_images.keys())[0]
        face_var.set(first)
        update_selected_face()
        update_face_menu()

def update_face_menu():
    menu = face_menu["menu"]
    menu.delete(0, "end")
    for name in overlay_images.keys():
        menu.add_command(label=name, command=lambda v=name: face_var.set(v))

def update_selected_face(*args):
    global overlay_image
    selected = face_var.get()
    overlay_image = overlay_images[selected]

# Camera selection
def list_cameras():
    available = []
    for i in range(5):
        cap_test = cv2.VideoCapture(i)
        if cap_test.isOpened():
            available.append(str(i))
            cap_test.release()
    return available

def update_camera_menu():
    menu = camera_menu["menu"]
    menu.delete(0, "end")
    for index in list_cameras():
        menu.add_command(label=index, command=lambda v=index: camera_var.set(v))
    if list_cameras():
        camera_var.set(list_cameras()[0])

# Overlay mask onto face
def add_overlay(frame, landmarks, overlay_img):
    try:
        left_eye = landmarks[33]
        right_eye = landmarks[263]
        nose = landmarks[1]

        eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
        dx = right_eye[0] - left_eye[0]
        dy = right_eye[1] - left_eye[1]
        angle = np.degrees(np.arctan2(dy, dx))

        face_width = int(np.linalg.norm(np.array(right_eye) - np.array(left_eye)) * 2)

        resized_overlay = cv2.resize(overlay_img, (face_width, face_width))
        rot_mat = cv2.getRotationMatrix2D((face_width // 2, face_width // 2), angle, 1.0)
        rotated_overlay = cv2.warpAffine(resized_overlay, rot_mat, (face_width, face_width), flags=cv2.INTER_LINEAR)

        x = int(nose[0] - face_width // 2)
        y = int(nose[1] - face_width // 2)

        for i in range(rotated_overlay.shape[0]):
            for j in range(rotated_overlay.shape[1]):
                if rotated_overlay[i, j, 3] != 0:
                    if 0 <= y+i < frame.shape[0] and 0 <= x+j < frame.shape[1]:
                        frame[y+i, x+j] = rotated_overlay[i, j, :3]
    except:
        pass
    return frame

# Start webcam
def start_camera():
    global cap, running
    if overlay_image is None:
        print("Select a face image first.")
        return
    running = True
    cap = cv2.VideoCapture(int(camera_var.get()))
    thread = threading.Thread(target=video_loop)
    thread.start()

# Stop webcam
def stop_camera():
    global running
    running = False

# Take snapshot and save to disk
def take_snapshot():
    global latest_frame
    if not os.path.exists("snapshots"):
        os.makedirs("snapshots")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"snapshots/snapshot_{timestamp}.png"
    if latest_frame is not None:
        cv2.imwrite(filename, cv2.cvtColor(latest_frame, cv2.COLOR_RGB2BGR))
        print(f"Snapshot saved: {filename}")
        return filename
    return None

# Run face swap on latest snapshot
def run_face_swap():
    snapshot_path = take_snapshot()
    if snapshot_path:
        target_face = os.path.join("face_masks", face_var.get())
        output_path = f"results/swapped_{datetime.datetime.now().strftime('%H%M%S')}.png"
        subprocess.run(["python", "face_swap.py", snapshot_path, target_face])
        print("Face swap process complete.")

# Main video loop
def video_loop():
    global cap, running, latest_frame
    while running:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                landmarks = []
                h, w, _ = frame.shape
                for lm in face_landmarks.landmark:
                    x, y = int(lm.x * w), int(lm.y * h)
                    landmarks.append((x, y))
                frame = add_overlay(frame, landmarks, overlay_image)

        latest_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(latest_frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    cap.release()

# GUI
app = Tk()
app.title("Fake Face - Full App")
app.geometry("900x700")

# GUI buttons
btn_load_faces = Button(app, text="Load Face Library", command=load_face_library)
btn_load_faces.pack()

face_menu = OptionMenu(app, face_var, "")
face_menu.pack()

camera_menu = OptionMenu(app, camera_var, "")
camera_menu.pack()

btn_refresh_cams = Button(app, text="Refresh Cameras", command=update_camera_menu)
btn_refresh_cams.pack()

btn_start = Button(app, text="Start Camera", command=start_camera)
btn_start.pack()

btn_stop = Button(app, text="Stop Camera", command=stop_camera)
btn_stop.pack()

btn_snapshot = Button(app, text="Take Snapshot", command=take_snapshot)
btn_snapshot.pack()

btn_faceswap = Button(app, text="Run Face Swap (GAN-like)", command=run_face_swap)
btn_faceswap.pack()

video_label = Label(app)
video_label.pack()

# Init
load_face_library()
update_camera_menu()

app.mainloop()
