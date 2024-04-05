import cv2
import os
import numpy as np
import time

dataPath = "../data/pruebas/emociones"
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = os.path.join(dataPath, nameDir)
    print("Leyendo las imágenes de", nameDir)

    for fileName in os.listdir(personPath):
        print("Rostros:", os.path.join(nameDir, fileName))
        labels.append(label)
        facesData.append(cv2.imread(os.path.join(personPath, fileName), 0))

    label += 1

# Crear el objeto reconocedor de rostros EigenFace
face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Entrenar el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenar el modelo obtenido
face_recognizer.save("../modelos/modeloEigenFaceEmociones.xml")

print("Modelo almacenado...")