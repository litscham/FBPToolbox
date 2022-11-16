#live plot of frame mean and fpa temp
mean=[]
fpa_tmp=[]
with Boson() as camera:
    camera.do_ffc()
    while True:
        frame = [] 
        frame=camera.grab()
        mean.append(frame)
        fpa_tmp.append(camera.get_fpa_temperature())
        std.append(np.std(pixel))
        plt.subplot(211)
        plt.plot(mean)
        plt.subplot(212)
        plt.plot(fpa_tmp)
        plt.show()
        clear_output(wait=True)
