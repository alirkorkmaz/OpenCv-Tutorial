import cv2
from pyrsistent import v

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

video_cod = cv2.VideoWriter_fourcc(*"XVID")
video_output = cv2.VideoWriter("../OpenCv/Goruntuler/video_me.avi", video_cod, 30,
                                (frame_width, frame_height))

while True: 
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Frame", frame)
        video_output.write(frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
video_output.release()