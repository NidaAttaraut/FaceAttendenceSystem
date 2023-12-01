import cv2
import numpy as np
import csv
from datetime import datetime
import face_recognition

from enroll_n_save import enroll_and_save_name

# Functions from Prompt 2
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

'''def mark_attendance(name, students, lnwriter):
    if name in known_faces_names and name in students:
        students.remove(name)
        print(students)
        current_time = datetime.now().strftime("%H-%M-%S")
        lnwriter.writerow([name, current_time])

# Mark Attendance Button (Triggering Function from Prompt 2)
def mark_attendance_ui():
    video_capture = cv2.VideoCapture(0)
    known_faces_data = load_enrolled_data()
    known_face_encodings = [data[1] for data in known_faces_data]
    known_faces_names = [data[0] for data in known_faces_data]
    students = known_faces_names.copy()

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

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            
            mark_attendance(name, students, lnwriter)
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
    f.close()'''

# Monthly attendance
'''import csv
from datetime import datetime
import cv2
import numpy as np
import face_recognition

known_faces_data = load_enrolled_data()
known_face_encodings = [data[1] for data in known_faces_data]
known_faces_names = [data[0] for data in known_faces_data]
now = datetime.now()
current_month = now.strftime("%B_%Y")

def mark_attendance(name, students, csv_writer, current_day):
    if name in known_faces_names and name in students:
        students.remove(name)
        print(students)

        # Mark attendance for the current day
        csv_writer.writerow({"ID": known_faces_names.index(name) + 1, "Full Name": name, f"{current_day}/{current_month}": 1})

def mark_attendance_ui():
    now = datetime.now()
    current_month = now.strftime("%B_%Y")
    current_day = now.day  # Get the current day of the month
    csv_filename = f"{current_month}_attendance.csv"

    with open(csv_filename, mode="a", newline="") as csv_file:
        fieldnames = ["ID", "Full Name"] + [f"{day}/{current_month}" for day in range(1, 31)]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the file is empty and write the header
        if csv_file.tell() == 0:
            csv_writer.writeheader()

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

            students = known_faces_names.copy()

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]

                    # Check if attendance is already marked for today
                    mark_attendance(name, students, csv_writer, current_day)

                face_names.append(name)

                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)
                cv2.putText(
                    frame, f"{name}", (left * 4, top * 4 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2
                )

            cv2.imshow("Attendance System", frame)

            #key = cv2.waitKey(1) & 0xFF
            if key == ord('e'):
                # You can add the enrollment code here if needed
                pass

            #if key == ord('q'):
                #break

    video_capture.release()
    cv2.destroyAllWindows()

# Call the modified function
mark_attendance_ui()'''



#Updated code of Monthly CSV
'''import csv
from datetime import datetime
import cv2
import numpy as np
import face_recognition

known_faces_data = load_enrolled_data()
known_face_encodings = [data[1] for data in known_faces_data]
known_faces_names = [data[0] for data in known_faces_data]

def mark_attendance_ui():
    now = datetime.now()
    current_month = now.strftime("%B_%Y")
    csv_filename = f"attendance_{current_month}.csv"

    with open(csv_filename, mode="a", newline="") as csv_file:
        fieldnames = ["ID", "Full Name", "Date"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the file is empty and write the header
        if csv_file.tell() == 0:
            csv_writer.writeheader()

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
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]

                    # Check if attendance is already marked for today
                    today_date = now.strftime("%Y-%m-%d")
                    csv_writer.writerow({"ID": best_match_index, "Full Name": name, "Date": today_date})
                    print(f"Marked attendance for {name} on {today_date}")

            cv2.imshow("Attendance System", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('e'):
                # You can add the enrollment code here if needed
                pass

            if key == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

# Call the modified function
mark_attendance_ui()'''


import csv
from datetime import datetime
import cv2
import numpy as np
import face_recognition

known_faces_data = load_enrolled_data()
known_face_encodings = [data[1] for data in known_faces_data]
known_faces_names = [data[0] for data in known_faces_data]
now = datetime.now()
current_month = now.strftime("%B_%Y")

# Initialize a set to keep track of students whose attendance has already been recorded
attendance_recorded = set()

def mark_attendance(name, students, csv_writer, current_day):
    if name in known_faces_names and name in students and name not in attendance_recorded:
        students.remove(name)
        attendance_recorded.add(name)
        print(students)

        # Mark attendance for the current day
        csv_writer.writerow({"ID": known_faces_names.index(name) + 1, "Full Name": name, f"{current_day}/{current_month}": 1})

def mark_attendance_ui():
    now = datetime.now()
    current_month = now.strftime("%B_%Y")
    current_day = now.day  # Get the current day of the month
    csv_filename = f"{current_month}_attendancerecord.csv"

    with open(csv_filename, mode="a", newline="") as csv_file:
        fieldnames = ["ID", "Full Name"] + [f"{day}/{current_month}" for day in range(1, 31)]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the file is empty and write the header
        if csv_file.tell() == 0:
            csv_writer.writeheader()

        video_capture = cv2.VideoCapture(0)
    
        #f = open(current_month + '.csv', "w+", newline="")
        #csv.writer(f)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Error: Could not open camera.")
                break

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            students = known_faces_names.copy()

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]

                    # Check if attendance is already marked for today
                    mark_attendance(name, students, csv_writer, current_day)

                face_names.append(name)

                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left * 4, top * 4), (right * 4, bottom * 4), (0, 255, 0), 2)
                cv2.putText(
                    frame, f"{name}", (left * 4, top * 4 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2
                )

            cv2.imshow("Attendance System", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('e'):
                # You can add the enrollment code here if needed
                pass

            if key == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()

# Call the modified function
mark_attendance_ui()


