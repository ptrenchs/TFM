import cv2
 
def nada(x):
    pass
 
img = cv2.imread("/home/ptrenchs/Escritorio/TFM/imagenes/puntos_0365.jpg")
#Redimensionarla imagen
filas, columnas, _ = img.shape
img = cv2.resize(img, (columnas//2, filas//2) )
#Usar blur
img = cv2.blur(img, (5,5))
#Crear la ventana y barras delizantes
cv2.namedWindow("Canny con barras")
cv2.createTrackbar("Umbral1", "Canny con barras", 0, 400, nada)
cv2.createTrackbar("Umbral2", "Canny con barras", 0, 400, nada)
while True:
    img2 = img.copy()
    a = cv2.getTrackbarPos("Umbral1", "Canny con barras")
    b = cv2.getTrackbarPos("Umbral2", "Canny con barras")
    imgCanny = cv2.Canny(img, a, b)
    #Encontrar y dibujar contornos
    contornos, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, contornos, -1, (0, 255, 0), 3)
 
    cv2.imshow("Canny con barras", imgCanny)
    cv2.imshow("Contornos", img2)
    if cv2.waitKey(1) == ord("s"):
        break
 
cv2.destroyAllWindows()