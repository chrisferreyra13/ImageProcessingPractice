from __future__ import print_function
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"]) #Objeto tipo numpy
print("width: {} pixels".format(image.shape[1]))    # El 1 es ancho
print("height: {} pixels".format(image.shape[0]))   # El 0 es alto
print("channels: {}".format(image.shape[2]))    # Los channels estan en el 3

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("output_image.png", image)