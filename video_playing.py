import cv2 

video_path = "../OpenCv/Goruntuler/video.mp4"

# videoCapture fonksiyonu birden fazla kare barındıran ard arda akan görsellerin tamamı için kullanılır
cap = cv2.VideoCapture(video_path)

# isOpened fpnksiyonu kare var mı yok mu diye kontrol ediyor
while cap.isOpened():

    ret, frame = cap.read()
    # ret ile videonun devam ettiğini sorgularız, video biterse kapanır
    if ret:
        cv2.imshow("Frame", frame)

        # 25 milisaniyede bir q'ya basıldığını kontrol et
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


