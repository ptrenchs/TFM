import cv2
import numpy as np

lista_areas = []

img = cv2.imread('/home/pol-trenchs/Escritorio/TFM/imagenes/puntos_0365.jpg')
filas,columnas,calnales = img.shape
# img = cv2.resize(img, (columnas * 2, filas * 2))
img = cv2.blur(img, (5,5))

# Aplicando Canny
canny = cv2.Canny(img, 20, 100)
# Aplicacion closing
kernel = np.ones((15,15))
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
    cv2.drawContours(img, contornos, i, (255,255,0), 2)
contorno_max = lista_areas.index(area_max)
cv2.drawContours(img, contornos, contorno_max, (0,255,0), 2)
[cv2.rectangle(img, esquina_superior_iz[i], esquina_complementaria[i], (0, 255, 255), 2) for i in range(len(contornos)) if i != contorno_max]
filas,columnas,calnales = img.shape
img = cv2.resize(img, (columnas // 2, filas // 2))

cv2.imshow('Siluetas', img)
# cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()