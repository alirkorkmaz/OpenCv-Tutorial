import cv2
# openCv y'den x'e giderek okuma yapar

image = cv2.imread("../OpenCv/Goruntuler/img.png")
image = cv2.resize(image, None, fx= 1/2, fy= 1/2, interpolation= cv2.INTER_AREA)

# belirtilen eksenler arasında kalan alanlar için kırpma yapar
x, y, w, h = 100, 50, 400, 400

# 50'den 400 kadar y ekseni için, 100'den 400'e kadar x ekseni için kırpma yapar
# openCv y'den x'e giderek okuma yapar
cropped_image = image[y:h, x:w]

cv2.imshow("Image", image)
cv2.imshow("Cropped Image", cropped_image)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()