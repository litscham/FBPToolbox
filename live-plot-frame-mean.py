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
        avg.append(np.mean(frame))
        mean = np.mean(avg)
        ax1.clear()
        ax2.clear()
        ax1.scatter(x,avg)
        ax1.hlines(mean,0,len(x),'r')
        ax1.text(0,mean,'mean %d'%mean)
        ax2.plot(x,fpa_tmp)

ani = FuncAnimation(fig, animate, interval=17)

plt.show()
