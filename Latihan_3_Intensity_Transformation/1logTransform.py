import cv2 
import numpy as np 

img = cv2.imread('Latihan_3_Intensity_Transformation/sample.jpg') 
 
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img) 

log_transformed = np.array(log_transformed, dtype = np.uint8) 
 
cv2.imwrite('log_transformed.jpg', log_transformed) 

# comment