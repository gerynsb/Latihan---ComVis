import numpy as np 
import cv2 as cv 

img = cv.imread('lenna.png', 0)
print(img)

rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()