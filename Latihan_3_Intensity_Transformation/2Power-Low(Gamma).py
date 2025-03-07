 
import cv2 
import numpy as np 
  
# Open the image. 
img = cv2.imread(r"D:\Dokumen Kuliah\Pemrograman di luar Pembelajaran\Computer Vision\Latihan_3_Intensity_Transformation\sample.jpg")


# Trying 4 gamma values. 
for gamma in [0.1, 0.5, 1.2, 2.2]: 
      
    # Apply gamma correction. 
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') 
  
    # Save edited images. 
    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected) 