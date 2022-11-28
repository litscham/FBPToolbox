from flirpy.camera.boson import Boson
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

avg=[]
x=[]
fpa_tmp=[]

fig, ax = plt.subplots()

def animate(i):
    with Boson() as camera:
        frame=camera.grab()
        x.append(i)
        avg.append(np.mean(frame))
        ax.clear()
        ax.plot(x,avg)

ani = FuncAnimation(fig, animate, interval=1000)

plt.show()
