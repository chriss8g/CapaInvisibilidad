import cv2
import numpy as np
from datetime import datetime

# Lee la fecha y hora actual
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")
# Define el nombre del archivo de video
video_name = f"video_{timestamp}.avi"

# Inicializar el objeto para grabar el video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(video_name, fourcc, 20.0, (640, 480))

# Inicializar la cámara
cap = cv2.VideoCapture(0)

lower = np.array([30, 100, 100])
upper = np.array([90, 255, 255])

# Tomar una foto
ret, img = cap.read()

namedWindow = "Video en tiempo real"
# Crear una ventana que ocupe toda la pantalla
cv2.namedWindow( namedWindow, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(namedWindow, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Capturar el frame de la cámara
    ret, frame = cap.read()


    # Convertir el frame a espacio de color HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Crear una máscara para los píxeles verdes en el rango definido
    mask = cv2.inRange(hsv_frame, lower, upper)

    # Reemplazar los píxeles verdes del frame con los píxeles de la imagen capturada
    frame[mask != 0] = img[mask != 0]

    # Mostrar el frame capturado
    cv2.imshow(namedWindow, frame)

    # Guardar el frame en el video
    out.write(frame)

    # Esperar hasta que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos utilizados
cap.release()
out.release()
cv2.destroyAllWindows()
