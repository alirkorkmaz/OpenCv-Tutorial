import cv2

image_path = "../OpenCv/Goruntuler/img.png"
#imread fonksiyonu görüntüleri BGR olarak okur
image = cv2.imread(image_path)

# BGR to Gray
# BGR to Gray seçilmesinin sebebi imread fonksiyonu görüntüleri BGR olarak okur
new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Gray Image", new_image)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()