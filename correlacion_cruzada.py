import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar las imágenes (asegúrate de que las imágenes estén en la misma carpeta o proporciona el camino adecuado)
imagen1 = cv2.imread('/home/ptrenchs/Escritorio/TFM/imagenes/video_prova/video_prova_1.png', cv2.IMREAD_GRAYSCALE)  # Cargar imagen1 en escala de grises
imagen2 = cv2.imread('/home/ptrenchs/Escritorio/TFM/imagenes/video_prova/video_prova_3.png', cv2.IMREAD_GRAYSCALE)  # Cargar imagen2 en escala de grises

# Verificar si las imágenes fueron cargadas correctamente
if imagen1 is None or imagen2 is None:
    print("Error al cargar las imágenes.")
    exit()

# Redimensionar las imágenes si tienen diferentes tamaños
if imagen1.shape != imagen2.shape:
    print("Redimensionando imagen2 a las dimensiones de imagen1.")
    imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

# Realizar la correlación cruzada utilizando la función cv2.matchTemplate
result = cv2.matchTemplate(imagen2, imagen1, cv2.TM_CCOEFF_NORMED)

# Encontrar el punto de máxima correlación
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# El desplazamiento es el punto donde se encuentra la máxima correlación
desplazamiento = max_loc
print(f"Desplazamiento encontrado: {desplazamiento}")

# Mostrar las imágenes originales y el resultado de la correlación
plt.figure(figsize=(12, 6))

# Mostrar la imagen original 1
plt.subplot(1, 3, 1)
plt.title("Imagen 1")
plt.imshow(imagen1, cmap='gray')

# Mostrar la imagen original 2
plt.subplot(1, 3, 2)
plt.title("Imagen 2")
plt.imshow(imagen2, cmap='gray')

# Mostrar la correlación cruzada
plt.subplot(1, 3, 3)
plt.title("Correlación")
plt.imshow(result, cmap='hot')
plt.colorbar()

plt.show()

# Visualizar el rectángulo donde ocurrió la máxima correlación en la imagen
top_left = desplazamiento
h, w = imagen1.shape
bottom_right = (top_left[0] + w, top_left[1] + h)

# Dibuja un rectángulo en la imagen2 para indicar la ubicación de la máxima correlación
imagen2_correlacionada = cv2.rectangle(imagen2.copy(), top_left, bottom_right, 255, 2)

# Mostrar la imagen con el rectángulo de correlación
plt.figure(figsize=(6, 6))
plt.imshow(imagen2_correlacionada, cmap='gray')
plt.title("Máxima correlación con rectángulo")
plt.show()