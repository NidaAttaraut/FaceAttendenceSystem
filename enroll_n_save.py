import cv2
import numpy as np
import csv
from datetime import datetime
import face_recognition

known_face_encodings = []
known_faces_names = []

# Functions from Prompt 1
def save_face_encoding(name, face_encoding):
    with open(f"{name}_encoding.npy", "wb") as file:
        np.save(file, face_encoding)

    known_face_encodings.append(face_encoding)
    known_faces_names.append(name)

def save_name_with_encoding_to_csv(name, face_encoding):
    with open("enrolled_data.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name] + face_encoding.tolist())

def enroll_and_save_name():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not open camera.")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)

            cv2.putText(
                frame, "Enter Name (or 'q' to finish):", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
            )
            cv2.imshow("Enroll New Person", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == 13:
                name = input("Enter the person's name: ")
                save_face_encoding(name, face_encoding)
                save_name_with_encoding_to_csv(name, face_encoding)
                print(f"{name} enrolled successfully!")
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()