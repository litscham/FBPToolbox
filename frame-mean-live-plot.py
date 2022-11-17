#live plot of frame mean and fpa temp
from flirpy.camera.boson import Boson
from matplotlib import pyplot as plt

mean=[]
fpa_tmp=[]
with Boson() as camera:
    camera.do_ffc()
    while True:
        frame=camera.grab()
        mean.append(np.mean(frame))
        fpa_tmp.append(camera.get_fpa_temperature())
        std.append(np.std(pixel))
        plt.subplot(211)
        plt.plot(mean)
        plt.subplot(212)
        plt.plot(fpa_tmp)
        plt.show()
        plt.clf()
