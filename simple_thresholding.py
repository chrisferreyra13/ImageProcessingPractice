import numpy as np    
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Image", image)

(T, thresh)=cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)  # 2arg: el threshold
cv2.imshow("Threshold binary", thresh)                          # 3arg: el maximo valor aplicado por encima de T

(T, thresh_inv)=cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold binary inverse", thresh_inv)

cv2.imshow("Coins", cv2.bitwise_and(image,image,mask=thresh_inv))
cv2.waitKey(0)
