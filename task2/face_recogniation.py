import os
import cv2
import numpy as np
import pickle  # optional to save/load labels

dataset_path = "dataset"
label_dict = {i:name for i, name in enumerate(os.listdir(dataset_path))}

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        label_id, confidence = recognizer.predict(roi_gray)
        name = label_dict.get(label_id, "Unknown")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)
    
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
