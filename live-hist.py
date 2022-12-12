#live histogram of frame means
from flirpy.camera.boson import Boson
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

avg=[]
x=[]

fig, ax = plt.subplots()

def animate(i):
    with Boson() as camera:
        frame=camera.grab()
        avg.append(np.mean(frame))
        ax.clear()
        ax.hist(avg,lw=1, edgecolor = "black")


ani = FuncAnimation(fig, animate, interval=17)

plt.show()