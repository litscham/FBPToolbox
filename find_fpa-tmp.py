#find steady state FPA temperature

from flirpy.camera.boson import Boson
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

avg=[]
x=[]
fpa_tmp=[]

fig, (ax1, ax2) = plt.subplots(2,1)

def animate(i):
    with Boson() as camera:
        frame=camera.grab()
        fpa_tmp.append(camera.get_fpa_temperature())
        x.append(i)
        ax1.clear()
        ax2.clear()
        ax1.imshow(frame)
        ax2.plot(x,fpa_tmp)
        if len(fpa_tmp)>50 and fpa_tmp[-1]==fpa_tmp[-50]:
            print("FPA Temperatur stabil bei:",fpa_tmp[-1])

ani = FuncAnimation(fig, animate, interval=20)

plt.show()