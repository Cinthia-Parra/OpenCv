import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/dialisis.jpg')

# Redimensionamos la base una sola vez
base = cv2.resize(img, (640, 480))

# Procesos
gris = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gris, 100, 150)

# Convertimos a BGR para poder apilar
gris_bgr = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
bordes_bgr = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)

# Apilamos
panel = np.hstack([base, gris_bgr, bordes_bgr])

# Escalamos si es necesario
escala = 0.5
panel = cv2.resize(panel, (int(panel.shape[1] * escala), int(panel.shape[0] * escala)))

# Convertimos de BGR a RGB para matplotlib
panel_rgb = cv2.cvtColor(panel, cv2.COLOR_BGR2RGB)

# Mostramos con matplotlib (esto tiene barra de herramientas: zoom, guardar, etc.)
plt.figure(figsize=(10, 5))
plt.imshow(panel_rgb)
plt.title('Original | Gris | Bordes')
plt.axis('off')  # Ocultar ejes si quieres
plt.show()
