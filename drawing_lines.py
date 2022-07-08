import cv2

image_path = "../OpenCv/Goruntuler/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, None, fx= 1/2, fy= 1/2, interpolation= cv2.INTER_AREA)
image_shape = image.shape

point1 = (int(image_shape[0]*0.1), int(image_shape[1]* 0.1))
point2 = (int(image_shape[0]*0.9), int(image_shape[1]* 0.9))
cv2.line(image, point1, point2, (0,0,220), thickness=2)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()