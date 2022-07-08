import cv2
import numpy as np
# openCv y'den x'e giderek okuma yapar

image = cv2.imread("../OpenCv/Goruntuler/img.png")
#image = cv2.resize(image, None, fx= 1/2, fy= 1/2, interpolation= cv2.INTER_AREA)
image = cv2.resize(image, (256,256))
image_shape = image.shape

image1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
image2 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
image3 = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Image 3", image3)

# rotasyon yapılan görseller birleştirildi
image_concat = np.concatenate((image1, image2, image3), axis= 1)
cv2.imshow("Image Concat", image_concat)

cv2.waitKey(0)
cv2.destroyAllWindows()