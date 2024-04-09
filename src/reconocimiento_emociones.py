import cv2
import os
import pandas as pd
import time

dataPath = "../data/imagenes"
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

face_recognizer = cv2.face.EigenFaceRecognizer_create()

# Leyendo el modelo
face_recognizer.read("../modelos/modeloEigenFaceEmociones2.xml")

# Abriendo el video
cap = cv2.VideoCapture("../data/pruebas/muchas_personas.mp4")

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Crear DataFrame para almacenar las emociones y el tiempo
df_emociones = pd.DataFrame(columns=['Persona', 'Emocion', 'Tiempo'])

# Inicializar contador de personas
contador_personas = 0
personas_detectadas = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    start_time = time.time()  # Registra el tiempo de inicio del procesamiento del fotograma
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        indice_predicho = result[0]
        distancia_prediccion = result[1]

        # Verificamos si la distancia de la predicción es menor que un umbral
        if distancia_prediccion < 5700:
            nombre_predicho = imagePaths[indice_predicho]
            cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Verificar si la persona ya fue detectada
            if nombre_predicho not in personas_detectadas:
                contador_personas += 1
                personas_detectadas[nombre_predicho] = f"Persona{contador_personas}"
                nombre_persona = f"Persona{contador_personas}"
            else:
                nombre_persona = personas_detectadas[nombre_predicho]

            end_time = time.time()  # Registra el tiempo de finalización del procesamiento del fotograma
            elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido en el procesamiento del fotograma

            # Almacenar la emoción y el tiempo en el DataFrame
            df_emociones = pd.concat([df_emociones, pd.DataFrame({'Persona': [nombre_persona], 'Emocion': [nombre_predicho], 'Tiempo': [elapsed_time]})], ignore_index=True)
        else:
            nombre_predicho = "Desconocido"
            cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Guardar DataFrame en un archivo CSV
df_emociones.to_csv("../data/resultados/emociones2.csv", index=False)





