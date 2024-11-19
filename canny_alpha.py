import cv2
import numpy as np

lista_areas = []

img = cv2.imread('/home/ptrenchs/Escritorio/TFM/imagenes/puntos_0365.jpg')
filas,columnas,calnales = img.shape
# img = cv2.resize(img, (columnas * 2, filas * 2))
img = cv2.blur(img, (5,5))

# Aplicando Canny
for i in range(2):
    for j in range(2):
        canny = cv2.Canny(img, 50 * (i + 1), 50 * (j + 1))
        cv2.imshow(f'Canny threshold1 {50 * (i + 1)} and threshold2 {50 * (j + 1)}', cv2.resize(canny, (columnas // 2, filas // 2)))

cv2.waitKey(0)
cv2.destroyAllWindows()