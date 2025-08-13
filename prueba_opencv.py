#import cv2
#
## Leer imagen (asegúrate de que exista en la misma carpeta)
#imagen = cv2.imread('dialisis.jpg')
#
## Mostrar imagen
#cv2.imshow('Imagen original', imagen)
#
## Cambiar tamaño a 640x480
#imagen = cv2.resize(imagen, (640, 480))
#
## Convertir a escala de grises
#gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Escala de grises', gris)
#
## Detectar bordes
#bordes = cv2.Canny(gris, 50, 150)
#cv2.imshow('Bordes', bordes)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()


import cv2

img = cv2.imread('dialisis.jpg')

# Redimensionar primero
img = cv2.resize(img, (640, 480))

# Ahora sí mostrar
cv2.imshow('Imagen original', img)

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de grises', gris)

bordes = cv2.Canny(gris, 50, 150)
cv2.imshow('Bordes', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()


