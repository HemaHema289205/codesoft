import os
import cv2
import numpy as np

dataset_path = "dataset"
label_dict = {}  # ID -> name
faces = []
labels = []

label_id = 0
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    if not os.path.isdir(person_folder):
        continue
    label_dict[label_id] = person_name
    
    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        faces.append(img)
        labels.append(label_id)
    
    label_id += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))
recognizer.save("face_model.yml")

print("✅ Training completed successfully")
print("Label Dictionary:", label_dict)
