#live view with video capture
import cv2
from flirpy.camera.boson import Boson
import numpy as np

video = cv2.VideoCapture(0)
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
result=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'),60, size)

with Boson() as camera:
    while True:
        img = camera.grab().astype(np.float32)
        img = 255*(img - img.min())/(img.max()-img.min())
        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)
        result.write(img_col)
        cv2.imshow('Boson',img_col)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
video.release()
result.release()
cv2.destroyAllWindows()
