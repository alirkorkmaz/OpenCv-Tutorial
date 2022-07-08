import cv2

video_path = 0 
# bilgisayarımda webcamim 0 id ile açılıyor
cap = cv2.VideoCapture(video_path)

# diğer tüm adımlar video ekleme  ile aynıdır
while cap.isOpened():

    ret, frame = cap.read()

    # frame videonun tandığı değişkendir, 
    # fx ve fy ile pencerenin boyutunu ayarlıyoruz
    # interpolation ve none değer araştırılacak
    if ret:
        frame = cv2.resize(frame, None, fx= 1/2, fy= 1/2, interpolation= cv2.INTER_LINEAR)
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()