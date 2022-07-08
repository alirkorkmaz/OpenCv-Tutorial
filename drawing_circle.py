import cv2

image_path = "../OpenCv/Goruntuler/img.png"

image = cv2.imread(image_path)
image = cv2.resize(image, None, fx= 1/2, fy= 1/2, interpolation= cv2.INTER_AREA)
image_shape = image.shape

# görüntünün merkez noktasını bulmak için kullanıyoruz
# yüksekliğin yarısı ve genişliğin yarısı merkez noktayı verir 
# center_point değişkenimizi tuple olarak tutuyoruz
center_point = (int(image_shape[0] * 0.5), int(image_shape[1] * 0.5))

radius = 100
cv2.circle(image, center_point, radius, (0,0,255), thickness= 2 )

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()