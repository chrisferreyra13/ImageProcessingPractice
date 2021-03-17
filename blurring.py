import numpy as np    
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

blurred=np.hstack([
    cv2.blur(image, (3,3)), # Filtro pasa bajos, promedio
    cv2.blur(image, (5,5)),
    cv2.blur(image,(7,7))
])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

blurred=np.hstack([
    cv2.GaussianBlur(image, (3,3), 0),  # El ultimo parametro es sigma, standard deviation, en la direccion x
    cv2.GaussianBlur(image, (5,5), 0),  # 0 significa que OpenCV la calcula sola a partir del tamaño del kernel
    cv2.GaussianBlur(image, (7,7), 0),
])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

blurred=np.hstack([
    cv2.medianBlur(image, 3),   # El filtro de la mediana sirve para remover salt an pepper
    cv2.medianBlur(image, 5),   # Utilizar para remover RUIDO
    cv2.medianBlur(image,7)     # Se pierden los bordes
])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# Para mantener los bordes y eliminar el ruido se usa el filtro bilateral, dos distribuciones gaussianas
blurred=np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),  # 2arg: tamaño del kernel
    cv2.bilateralFilter(image, 7, 31, 31),  # 3arg: cantidad de intensidades tenidas en cuenta
    cv2.bilateralFilter(image, 9, 41, 41)   # 4arg: cuantos pixeles fuera del centro son tenidos en cuenta
])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)