import cv2
import numpy as np
import os

img = cv2.imread('/home/pol-trenchs/Escritorio/TFM/imagenes/puntos_0365.jpg')
print(np.shape(img))
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarizar la imagen
_, thr = cv2.threshold(img_gris, 150, 255, cv2.THRESH_BINARY)

# Kernel
kernel = np.ones((3,3), np.uint8)

# Erosion
erosion = cv2.erode(thr, kernel)
# Mostrar las imagenes
# cv2.imshow('imagen original', img)
cv2.imshow('Imagen gris', img_gris)
cv2.imshow('Imagen binarizada', thr)
cv2.imshow('imajen erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
