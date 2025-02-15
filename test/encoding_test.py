import face_recognition
import numpy as np

elon1_face = face_recognition.load_image_file("assets/training/elon_musk/161881.jpg")

elon1_encoding = face_recognition.face_encodings(elon1_face)

elon2_face = face_recognition.load_image_file("assets/training/elon_musk/161888.jpg")

elon2_encoding = face_recognition.face_encodings(elon2_face)

min_distance = float("inf")
booleen_val = face_recognition.compare_faces(elon1_encoding, elon2_encoding[0])
print(booleen_val)

distance = np.linalg.norm(elon1_encoding[0] - elon2_encoding)

if distance < min_distance and distance < 0.6:
    min_distance = distance
    print(True)