import argparse
import numpy as np
from skimage import io
from skimage import color
from skimage import filters
from skimage import util
from skimage import measure
from scipy import ndimage as ndi


ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args=vars(ap.parse_args())

coins=io.imread(args["image"])
coins_bw=color.rgb2gray(coins)
coins_f=filters.gaussian(coins_bw,sigma=1)
io.imshow(coins_f)
io.show()
threshold_value=filters.threshold_otsu(coins_f)

coins_t=coins_f.copy()
coins_t[coins_t>threshold_value]=1
coins_t[coins_t<threshold_value]=0

coins_r=util.invert(coins_t)


#coins_fill=ndi.binary_fill_holes(coins_r)

io.imshow(coins_r)
io.show()
contours=measure.find_contours(coins_r)


coins_contorno=color.gray2rgb(coins_r)

for contour in contours:
    for point in contour:
        coins_contorno[int(point[0]),int(point[1])]=[0,255,0]

io.imshow(coins_contorno)
io.show()