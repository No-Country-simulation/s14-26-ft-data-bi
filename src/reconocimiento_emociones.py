import cv2
import os

dataPath = "../data/pruebas/emociones"
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Leyendo el modelo
face_recognizer.read("../modelos/modeloEigenFaceEmociones.xml")

# Abriendo el video
cap = cv2.VideoCapture("../data/pruebas/persona_enojada.mp4")

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)


        indice_predicho = result[0]
        distancia_prediccion = result[1]

        # Verificamos si la distancia de la predicción es menor que un umbral
        if distancia_prediccion < 5700:
            nombre_predicho = imagePaths[indice_predicho]
            cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Desconocido", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()