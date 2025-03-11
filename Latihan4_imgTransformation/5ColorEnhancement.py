import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('Lenna.png')

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(image)

image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

image[:, :, 0] = image[:, :, 0] * 0.7
image[:, :, 1] = image[:, :, 1] * 1.5
image[:, :, 2] = image[:, :, 2] * 0.5 

image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

cv2.imwrite('enhanced coloured.jpg', image2)

plt.subplot(1, 2, 1)
plt.title('Color Enhanced')
plt.imshow(image2)
plt.show()