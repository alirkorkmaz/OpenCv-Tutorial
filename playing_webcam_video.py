import cv2

video_path = 0 
# bilgisayarımda webcamim 0 id ile açılıyor
cap = cv2.VideoCapture(video_path)

# diğer tüm adımlar video ekleme  ile aynıdır
while cap.isOpened():

    ret, frame = cap.read()

    if ret:

        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()