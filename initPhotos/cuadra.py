import cv2 as cv
import numpy as np

# Carga la imagen desde disco
img = cv.imread('images/dialisis.jpg')  

# Convierte a escala de grises para facilitar el procesamiento
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Aplica desenfoque para reducir ruido
blur = cv.GaussianBlur(gray, (5, 5), 0)

# Detecta bordes usando Canny (encontrará el contorno de la bolsa)
edges = cv.Canny(blur, 50, 150)

# Encuentra todos los contornos en la imagen
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Elege el contorno más grande (probablemente sea la bolsa)
bag_contour = max(contours, key=cv.contourArea)

# Dibuja ese contorno sobre la imagen (en azul) para visualizarlo
cv.drawContours(img, [bag_contour], -1, (255, 0, 0), 2)

# Define los rectángulos de verificación (debes ajustar esto según tu zona esperada)
outer_rect = (90, 20, 460, 440)   # rectángulo grande
inner_rect = (130, 60, 380, 360)  # rectángulo más pequeño

# Dibuja ambos rectángulos (verde claro y oscuro)
cv.rectangle(img, 
        (outer_rect[0], outer_rect[1]), 
        (outer_rect[0]+outer_rect[2], outer_rect[1]+outer_rect[3]), 
        (0, 255, 0), 3)  # verde claro

cv.rectangle(img, 
        (inner_rect[0], inner_rect[1]), 
        (inner_rect[0]+inner_rect[2], inner_rect[1]+inner_rect[3]), 
        (0, 128, 0), 3)  # verde oscuro

# Verifica si las esquinas del rectángulo interior están dentro del contorno de la bolsa
corners = [
        (inner_rect[0], inner_rect[1]),  # esquina superior izquierda
        (inner_rect[0] + inner_rect[2], inner_rect[1]),  # esquina superior derecha
        (inner_rect[0], inner_rect[1] + inner_rect[3]),  # esquina inferior izquierda
        (inner_rect[0] + inner_rect[2], inner_rect[1] + inner_rect[3])  # esquina inferior derecha
]

# Usa pointPolygonTest para verificar si cada esquina está dentro del contorno
ok = all(cv.pointPolygonTest(bag_contour, corner, False) >= 0 for corner in corners)

# Muestra resultado en consola
if ok:
        print("✅ Bolsa correctamente posicionada.")
else:
        print("❌ Bolsa MAL posicionada.")

# MUestra la imagen con los resultados
cv.imshow("Verificación de posicionamiento", img)
cv.waitKey(0)
cv.destroyAllWindows()
