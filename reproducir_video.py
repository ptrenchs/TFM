import cv2
import numpy as np

def bordes(img):
    img_copy = img.copy()
    lista_areas = []

    # img_copy = cv2.imread('/home/ptrenchs/Escritorio/TFM/imagenes/puntos_0365.jpg')
    filas,columnas,calnales = img_copy.shape
    # img_copy = cv2.resize(img_copy, (columnas * 2, filas * 2))
    img_copy = cv2.blur(img_copy, (5,5))

    # Aplicando Canny
    canny = cv2.Canny(img_copy, 20, 100)
    # Aplicacion closing
    kernel = np.ones((15,15))
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)


    contornos = []
    n = 10
    cont = 0
    while True:
        kernel = np.ones((n,n))
        closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
        contornos_frame,_ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contornos_frame) == len(contornos):
            cont += 1
            if cont<10:
                n += 2 
        else:
            cont = 0
            n += 2
        contornos = contornos_frame
        if 10 < cont:
            break

    esquina_superior_iz = []
    esquina_complementaria = []
    centros = []
    for i in range(len(contornos)):
        # print(contornos[i])
        x, y, w, h = cv2.boundingRect(contornos[i])
        # Dibujar el rectángulo en la imagen original
        esquina_superior_iz.append((x,y))
        esquina_complementaria.append((x + w, y + h))
        # cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cx = x + w // 2
        cy = y + h // 2
        centros.append((cx, cy))
        area = cv2.contourArea(contornos[i])
        lista_areas.append(area)
        area_max = max(lista_areas)
        cv2.drawContours(img_copy, contornos, i, (255,255,0), 2)
    contorno_max = lista_areas.index(area_max)
    cv2.drawContours(img_copy, contornos, contorno_max, (0,255,0), 2)
    [cv2.rectangle(img_copy, esquina_superior_iz[i], esquina_complementaria[i], (0, 255, 255), 2) for i in range(len(contornos)) if i != contorno_max]
    filas,columnas,calnales = img_copy.shape
    img_copy = cv2.resize(img_copy, (columnas // 2, filas // 2))
    return img_copy
    # cv2.imshow('Siluetas', img_copy)

# Ruta al archivo de video
ruta_video = '/home/ptrenchs/Escritorio/videos/prova_1.mp4'

# Crear un objeto VideoCapture para leer el video
video = cv2.VideoCapture(ruta_video)

# Comprobar si el video se ha abierto correctamente
if not video.isOpened():
    print("Error al abrir el video.")
    exit()

# Leer y mostrar los fotogramas del video en un bucle
while True:
    ret, fotograma = video.read()  # Leer el siguiente fotograma
    if not ret:  # Si no hay más fotogramas, salir del bucle
        break
    
    fotograma = bordes(fotograma)
    # Mostrar el fotograma en una ventana
    cv2.imshow('Video', fotograma)

    # Esperar 25 ms y salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y cerrar las ventanas
video.release()
cv2.destroyAllWindows()
