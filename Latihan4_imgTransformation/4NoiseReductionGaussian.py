import cv2
import matplotlib.pyplot as plt 
import numpy as np 

image = cv2.imread('Lenna.png')

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(image)

# Menggunakan Gaussian Blur
filtered_image2 = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imwrite('Gaussian Blur.jpg', filtered_image2)

plt.subplot(1, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(filtered_image2)
plt.show()