import cv2
import matplotlib.pyplot as plt
import numpy as np 

image = cv2.imread('Lenna.png')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

sharpened_image2 = cv2.Laplacian(image, cv2.CV_64F)

cv2.imwrite('Laplacian_sharpened_image.jpg', sharpened_image2)

plt.subplot(1, 2, 1)
plt.title("Laplacian Sharpening")
plt.imshow(sharpened_image2)
plt.show()