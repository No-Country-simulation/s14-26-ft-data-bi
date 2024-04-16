# import cv2
# import os
# import pandas as pd
# import time

# ruta_video ="../data/pruebas/clase1.mp4"
# dataPath = "../data/imagenes"

# def reconocimiento_emociones(ruta_video):
#     imagePaths = os.listdir(dataPath)
#     emociones_dict = {idx: emocion for idx, emocion in enumerate(imagePaths)}
    
#     face_recognizer = cv2.face.EigenFaceRecognizer_create()
#     face_recognizer.read("../modelos/modeloEigenFaceEmociones2.xml")

#     cap = cv2.VideoCapture(ruta_video)
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#     df_emociones = []
#     contador_personas = 0
#     personas_detectadas = {}

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Tiempo actual del fotograma en segundos

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         auxFrame = gray.copy()
#         faces = faceClassif.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             rostro = auxFrame[y:y+h, x:x+w]
#             rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
#             result = face_recognizer.predict(rostro)

#             indice_predicho = result[0]
#             distancia_prediccion = result[1]

#             nombre_predicho = emociones_dict.get(indice_predicho, "Desconocido")
#             color = (0, 255, 0) if distancia_prediccion < 5700 else (0, 0, 255)

#             cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

#             if nombre_predicho not in personas_detectadas:
#                 contador_personas += 1
#                 personas_detectadas[nombre_predicho] = f"Persona{contador_personas}"
#                 nombre_persona = f"Persona{contador_personas}"
#             else:
#                 nombre_persona = personas_detectadas[nombre_predicho]

#             df_emociones.append({'Persona': nombre_persona, 'Emocion': nombre_predicho, 'Tiempo_Inicio': frame_time, 'Tiempo_Fin': frame_time + (1 / fps)})

#         cv2.imshow('frame', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     df_emociones = pd.DataFrame(df_emociones)
#     df_emociones.to_csv("../data/resultados/emociones3.csv", index=False)

# reconocimiento_emociones(ruta_video)

# import cv2
# import os
# import pandas as pd

# ruta_video = "../data/pruebas/clase2.mp4"
# dataPath = "../data/imagenes"

# def reconocimiento_emociones(ruta_video):
#     imagePaths = os.listdir(dataPath)
#     emociones_dict = {idx: emocion for idx, emocion in enumerate(imagePaths)}
    
#     face_recognizer = cv2.face.EigenFaceRecognizer_create()
#     face_recognizer.read("../modelos/modeloEigenFaceEmociones2.xml")

#     cap = cv2.VideoCapture(ruta_video)
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#     cantidad_personas = 0  # Variable para contar la cantidad de personas

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Tiempo actual del fotograma en segundos

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         auxFrame = gray.copy()
#         faces = faceClassif.detectMultiScale(gray, 1.3, 5)

#         # Contar la cantidad de personas en el video
#         cantidad_personas = len(faces)

#         for i, (x, y, w, h) in enumerate(faces, start=1):
#             rostro = auxFrame[y:y+h, x:x+w]
#             rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
#             result = face_recognizer.predict(rostro)

#             indice_predicho = result[0]
#             distancia_prediccion = result[1]

#             nombre_predicho = emociones_dict.get(indice_predicho, "Desconocido")
#             color = (0, 255, 0) if distancia_prediccion < 5700 else (0, 0, 255)

#             cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

#             # Mostrar número único para cada persona
#             cv2.putText(frame, str(i), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

#             # Imprimir datos línea por línea
#             print(f'Persona: {i}, Emoción: {nombre_predicho}, Tiempo_Inicio: {frame_time}, Tiempo_Fin: {frame_time + (1 / fps)}')

#         cv2.imshow('frame', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     print("Cantidad de personas en el video:", cantidad_personas)

# reconocimiento_emociones(ruta_video)

















# ---------------------------
import cv2
import os
import pandas as pd

ruta_video = "../data/pruebas/clase3.mp4"
dataPath = "../data/imagenes"

def reconocimiento_emociones(ruta_video):
    imagePaths = os.listdir(dataPath)
    emociones_dict = {idx: emocion for idx, emocion in enumerate(imagePaths)}
    
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read("../modelos/modeloEigenFaceEmociones2.xml")

    cap = cv2.VideoCapture(ruta_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    df_emociones = []
    personas_detectadas = {}  # Diccionario para mantener un seguimiento de las personas detectadas
    contador_personas = 0  # Contador para asignar números únicos a las personas

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Tiempo actual del fotograma en segundos

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Verificar si la persona ya fue detectada anteriormente
            persona_id = None
            for coords, pid in personas_detectadas.items():
                cx, cy = coords
                if abs(x - cx) < 100 and abs(y - cy) < 100:  # Ampliar el espacio de búsqueda
                    persona_id = pid
                    break
            
            if persona_id is None:
                # Asignar un nuevo número de persona
                contador_personas += 1
                persona_id = contador_personas
                personas_detectadas[(x, y)] = persona_id

            # Mostrar el número de persona en el vídeo
            cv2.putText(frame, str(persona_id), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Procesar la emoción
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            indice_predicho = result[0]
            distancia_prediccion = result[1]

            nombre_predicho = emociones_dict.get(indice_predicho, "Desconocido")
            color = (0, 255, 0) if distancia_prediccion < 5700 else (0, 0, 255)

            cv2.putText(frame, nombre_predicho, (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

            df_emociones.append({'Persona': persona_id, 'Emocion': nombre_predicho, 'Tiempo_Inicio': frame_time, 'Tiempo_Fin': frame_time + (1 / fps)})

            # Imprimir datos en consola
            print(f'Persona: {persona_id}, Emoción: {nombre_predicho}, Tiempo_Inicio: {frame_time}, Tiempo_Fin: {frame_time + (1 / fps)}')

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Guardar los datos en un archivo CSV
    df_emociones = pd.DataFrame(df_emociones)
    df_emociones.to_csv("../data/resultados/emociones12.csv", index=False)

reconocimiento_emociones(ruta_video)






