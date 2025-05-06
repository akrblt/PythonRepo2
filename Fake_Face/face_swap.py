import face_recognition
import cv2
import numpy as np
import sys
import os

def swap_faces(src_path, target_path, output_path="results/output.png"):
    src_img = cv2.imread(src_path)
    target_img = cv2.imread(target_path)

    src_face_locations = face_recognition.face_locations(src_img)
    target_face_locations = face_recognition.face_locations(target_img)

    if not src_face_locations or not target_face_locations:
        print("Face not detected in one of the images.")
        return

    src_face_encoding = face_recognition.face_encodings(src_img, known_face_locations=src_face_locations)[0]
    src_face_landmarks = face_recognition.face_landmarks(src_img, known_face_locations=src_face_locations)[0]

    top, right, bottom, left = target_face_locations[0]
    target_face_image = target_img[top:bottom, left:right]

    center_point = ((left + right) // 2, (top + bottom) // 2)

    mask = 255 * np.ones(target_face_image.shape, target_face_image.dtype)

    blended = cv2.seamlessClone(src_img, target_img, mask, center_point, cv2.NORMAL_CLONE)

    if not os.path.exists("results"):
        os.makedirs("results")

    cv2.imwrite(output_path, blended)
    print(f"Face swap completed. Saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python face_swap.py [source_image] [target_image]")
    else:
        swap_faces(sys.argv[1], sys.argv[2])
