import numpy as np 
import cv2
from matplotlib import pyplot as plt

image_path = r'Latihan_2_Fourier_Transformation/Dhoni-dive_165121_730x419-m.jpg'
image = cv2.imread(image_path, 0)

DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

shift = np.fft.fftshift(DFT)
row, col = image.shape
center_row, center_col = row // 2, col // 2

mask = np.zeros((row, col, 2), np.uint8)
mask[center_row - 30:center_row + 30, center_col - 30:center_col + 30] = 1

fft_shift = shift * mask
fft_ifft_shift = np.fft.ifftshift(fft_shift)
imageThen = cv2.idft(fft_ifft_shift)

imageThen = cv2.magnitude(imageThen[:,:,0], imageThen[:,:,1])


plt.figure(figsize=(10,10))
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(imageThen, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()