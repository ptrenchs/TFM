import cv2
import numpy as np
import os

img = cv2.imread('/home/ptrenchs/Escritorio/TFM/imagenes/puntos_0365.jpg')
# print(img)
cv2.imshow("imagen original", img)
# img_gris = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

# # Binarizar la imagen
# _, thr = cv2.threshold(img_gris, 80, 255, cv2.THRESH_BINARY)

# # Mostrar las imagenes
# cv2.imshow('imagen original', img)
# cv2.imshow('Imagen gris', img_gris)
# cv2.imshow('Imagen binarizada', thr)
cv2.waitKey(0)
cv2.destroyAllWindows()
