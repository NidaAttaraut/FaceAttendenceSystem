import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)


Nida_image = face_recognition.load_image_file("C:/Users/Abbasali/OneDrive/Desktop/Face-recognition-based-attendance-system-master/face recognition source code/Photos/Nida.jpg")
Nida_encoding = face_recognition.face_encodings(Nida_image)[0]

Abbas_image = face_recognition.load_image_file("C:/Users/Abbasali/OneDrive/Desktop/Face-recognition-based-attendance-system-master/face recognition source code/Photos/Abbas.jpg")
Abbas_encoding = face_recognition.face_encodings(Abbas_image)[0]

t_image = face_recognition.load_image_file("C:/Users/Abbasali/OneDrive/Desktop/Face-recognition-based-attendance-system-master/face recognition source code/Photos/t.jpg")
t_encoding = face_recognition.face_encodings(t_image)[0]

i_image = face_recognition.load_image_file("C:/Users/Abbasali/OneDrive/Desktop/Face-recognition-based-attendance-system-master/face recognition source code/Photos/i.jpg")
i_encoding = face_recognition.face_encodings(t_image)[0]
                                                    


known_face_encoding =[
Nida_encoding,
Abbas_encoding,
t_encoding,
i_encoding
]



known_faces_names=[
"Nida",
"Abbas",
"Tesla",
"i"
]
students = known_faces_names.copy()
face_locations = []
face_encodings = []
face_names = []
s = True
 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
 
f = open(current_date+'.csv',"w+",newline = "")
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)

            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

    cv2.imshow("attendance system", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
f.close()   
