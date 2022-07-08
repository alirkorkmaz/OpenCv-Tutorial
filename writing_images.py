import cv2 

image_path = "../OpenCv/Goruntuler/img.png"
image = cv2.imread(image_path)

new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("../OpenCv/Goruntuler/gray_image.png")