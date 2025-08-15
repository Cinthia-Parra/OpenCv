import cv2 as cv
import numpy as np

# Cargar imagen y redimensionar
img = cv.imread("dialisis2.jpg")
img = cv.resize(img, (640, 480))

# Convertir a gris y aplicar desenfoque
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 0)

# Detección de bordes
edges = cv.Canny(blur, 50, 150)

# Crear una matriz (kernel) de 5x5 con unos, tipo uint8
kernel = np.ones((5, 5), np.uint8)

# Aplicar operación morfológica de cierre (cierra huecos y une bordes rotos)
closed = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)


# Encontrar contornos
contornos, _ = cv.findContours(closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Recorrer contornos encontrados
for c in contornos:
    area = cv.contourArea(c)
    #print(f"Área detectada: {area}")
    if area > 10000:  # regla simple
        x, y, w, h = cv.boundingRect(c)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # dibujar contorno
        cv.putText(img, "OK", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        x, y, w, h = cv.boundingRect(c)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # en rojo si no cumple
        cv.putText(img, "NG", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# Mostrar el área del contorno en consola (útil para ajustar umbrales de filtrado)
print("Área detectada:", area)
# Mostrar resultado
cv.imshow("Detección de Objetos", img)
cv.waitKey(0)
cv.destroyAllWindows()




