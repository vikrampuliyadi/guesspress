import cv2
import numpy as np

# put some random mp4 file here
video = cv2.VideoCapture("/Users/vikrampuliyadi/Downloads/bopkrish_hRJGm7W5.mp4")

if not video.isOpened():
    print("error")
    exit()

while True:

    _, frame = video.read()
    cv2.imshow("Video", frame)
    
    key = cv2.waitKey(30)

    if key == 27:
        break
video.release()
cv2.destroyAllWindows()

