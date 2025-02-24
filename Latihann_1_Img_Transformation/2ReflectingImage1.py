import numpy as np 
import cv2 as cv

img = cv.imread('Lenna.png', 0)
rows, cols = img.shape

# Flip Vertical
M = np.float32([[1, 0, 0],
                [0, -1, rows],
                [0, 0, -1]])

# Flip Horizontal
# M = np.float32([[-1, 0, cols], 
#                 [0, 1, 0], 
#                 [0, 0, 1]])


reflected_img = cv.warpPerspective(img, M,
                                   (int(cols),
                                    int(rows)))
cv.imshow('img', reflected_img)
cv.waitKey(0)
cv.destroyAllWindow()