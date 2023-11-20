import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

known_face_encodings = []
known_faces_names = []
students = known_faces_names.copy()




# Part 1: Enroll New Persons and Save Names with Encodings to CSV

def save_face_encoding(name, face_encoding):
    # Save the face encoding to a file or database
    # In this example, we'll save it to a file
    with open(f"{name}_encoding.npy", "wb") as file:
        np.save(file, face_encoding)

    # Add the new face encoding and name to the lists
    known_face_encodings.append(face_encoding)
    known_faces_names.append(name)

def save_name_with_encoding_to_csv(name, face_encoding):
    # Save the name and face encoding to a CSV file
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
            # Draw a rectangle around the face
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)

            # Display the name and ask the user to input the name
            cv2.putText(frame, "Enter Name (or 'q' to finish):", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow("Enroll New Person", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == 13:  # Enter key is pressed
                name = input("Enter the person's name: ")
                save_face_encoding(name, face_encoding)
                save_name_with_encoding_to_csv(name, face_encoding)
                print(f"{name} enrolled successfully!")
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

# Uncomment the following line to enroll new persons
enroll_and_save_name()




# Part 2: Mark Attendance with Name and ID

video_capture = cv2.VideoCapture(0)

# Function to load enrolled data from CSV
def load_enrolled_data():
    enrolled_data = []
    try:
        with open("enrolled_data.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                name = row[0]
                encoding = np.array(list(map(float, row[1:])))
                enrolled_data.append((name, encoding))
    except FileNotFoundError:
        pass
    return enrolled_data

# Initialize variables
known_faces_data = load_enrolled_data()
known_face_encodings = [data[1] for data in known_faces_data]
known_faces_names = [data[0] for data in known_faces_data]

students = known_faces_names.copy()
face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + '.csv', "w+", newline="")
lnwriter = csv.writer(f)


while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Could not open camera.")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
                name = known_faces_names[best_match_index]

        face_names.append(name)

        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)
        cv2.putText(frame, f"{name}", (left * 4, top * 4 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

# Display the list of students present
    #print("Students Present:", students)

    cv2.imshow("Attendance System", frame)

    # Ask whether to enroll a new person before marking attendance
    key = cv2.waitKey(1) & 0xFF
    if key == ord('e'):
        enroll_and_save_name()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

video_capture.release()
cv2.destroyAllWindows()
f.close()
