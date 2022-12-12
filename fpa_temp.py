#find steady state FPA temperature

from flirpy.camera.boson import Boson
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
frame=[]
with Boson() as camera:
    camera.set_ffc_manual()
    while len(frame) < 100000:
        start = time.time()
        frame.append(camera.grab())
        end = time.time()
        print(end - start)
