import cv2
import numpy as np

img = cv2.imread('dialisis.jpg')

# Redimensionamos la base una sola vez
base = cv2.resize(img, (640, 480))

# Procesos
gris = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gris, 50, 150)

# Para apilar, convierte gris y bordes a BGR
gris_bgr = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
bordes_bgr = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)

# Apilar horizontalmente
panel = np.hstack([base, gris_bgr, bordes_bgr])

# Si queda muy ancho, puedes escalarlo (por ejemplo al 70%)
escala = 0.5
panel = cv2.resize(panel, (int(panel.shape[1]*escala), int(panel.shape[0]*escala)))


        # Muestra la imagen 'panel' con este título
cv2.imshow('Original | Gris | Bordes', panel)

        # Espera hasta que se presione una tecla
cv2.waitKey(0)

        # Cierra todas las ventanas abiertas
cv2.destroyAllWindows()
