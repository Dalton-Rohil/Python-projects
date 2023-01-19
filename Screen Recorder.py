import cv2
import numpy as np
import pyautogui

fourcc = cv2.VideoWriter_fourcc(*"XVID")

screen_size = (1920, 1080)
fps = 30.0

out = cv2.VideoWriter("screen_recording.avi", fourcc, fps, screen_size)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Screen Recording", frame)
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()
