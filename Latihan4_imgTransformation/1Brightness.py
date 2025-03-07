import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

image = cv2.imread('Lenna.png')

plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(image)


# Mengontrol brightness 
brightness = 10

# Mengontrol contrast
contrast = 2.3
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

cv2.imwrite('lenna_brightness.jpg', image2)

plt.subplot(1, 2, 2)
plt.title('Brightness & Contrast')
plt.show()