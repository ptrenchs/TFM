import cv2
import numpy as np
import os

def contornos(img):

    lista_areas = []

    img_copy = img.copy()
    # img = cv2.imread('/home/ptrenchs/Escritorio/TFM/imagenes/puntos_0365.jpg')
    filas,columnas,calnales = img_copy.shape
    # img_copy = cv2.resize(img_copy, (columnas * 2, filas * 2))
    img_copy = cv2.blur(img_copy, (5,5))
    canny = cv2.Canny(img, 20, 100)
    kernel = np.ones((20,20))
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    contornos,_ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    esquina_superior_iz = []
    esquina_complementaria = []
    centros = []

    for i in range(len(contornos)):
        # print(contornos[i])
        x, y, w, h = cv2.boundingRect(contornos[i])
        # Dibujar el rectángulo en la imagen original
        esquina_superior_iz.append((x,y))
        esquina_complementaria.append((x + w, y + h))
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cx = x + w // 2
        cy = y + h // 2
        centros.append((cx, cy))
        area = cv2.contourArea(contornos[i])
        lista_areas.append(area)
        area_max = max(lista_areas)
        # cv2.drawContours(img, contornos, i, (255,255,0), 2)

    contorno_max = lista_areas.index(area_max)
    cv2.drawContours(img, contornos, contorno_max, (0,255,0), 2)
    # [cv2.rectangle(img, esquina_superior_iz[i], esquina_complementaria[i], (0, 255, 255), 2) for i in range(len(contornos)) if i != contorno_max]
    # filas,columnas,calnales = img.shape
    # img = cv2.resize(img, (columnas // 2, filas // 2))
    return img

# Crear un objeto VideoCapture para leer el video
video = cv2.VideoCapture(0)

# Comprobar si el video se ha abierto correctamente
if not video.isOpened():
    print("Error al abrir el video.")
    exit()

# Leer y mostrar los fotogramas del video en un bucle
dir_carpeta = '/home/ptrenchs/Escritorio/TFM/imagenes'
nombre_carpeta = 'video_prova'
nuew_carpeta = dir_carpeta + '/' + nombre_carpeta
if not os.path.exists(nuew_carpeta):
    os.makedirs(nuew_carpeta)
nombre = nombre_carpeta

n = 0
while True:
    ret, fotograma = video.read()  # Leer el siguiente fotograma
    if not ret:  # Si no hay más fotogramas, salir del bucle
        break
    fotograma_copy = fotograma.copy()
    # fotograma = contornos(fotograma)
    # Mostrar el fotograma en una ventana
    cv2.imshow('Video', fotograma)

    i = 0
    while True:
        dir_img = nuew_carpeta + '/' + nombre + '_' + str(n+1+i) + '.png'
        if not os.path.exists(dir_img):
            break
        i += 1

    cv2.imwrite(dir_img,fotograma_copy)
    # Esperar 25 ms y salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(25) & 0xFF == ord('q') or 10 < n:
        break
    n += 1
# Liberar el objeto VideoCapture y cerrar las ventanas
video.release()
cv2.destroyAllWindows()