import cv2

image_path = "../OpenCv/Goruntuler/img.png"  # görsel dosyamızın yolu
image = cv2.imread(image_path)  # imread ile görsel tipi farketmeksizin dosyalarımızı okumaya yarıyor

cv2.imshow("Image",image) # görselin gözükmesini sağlıyor fakat anlık gidip geliyor

cv2.waitKey(0)  # kapat tuşuna basmadan sekmenin kapanmasını istiyorum
cv2.destroyAllWindows()  # eğer kapatmak istiyorsak tüm seklemlerin kapanmasını istiyorum
 