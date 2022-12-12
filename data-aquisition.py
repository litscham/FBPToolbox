#data aquisition 
from flirpy.camera.boson import Boson
import numpy as np
import os
from time import sleep

temp = np.arange(50,80.5,0.5)
with Boson() as camera:
    while camera.get_fpa_temperature() < 43.8:
        print("warten bis 44 Grad erreicht sind. Aktuell:"+str(camera.get_fpa_temperature()))
        tmp=camera.grab()
        os.system('cls' if os.name == 'nt' else 'clear')
    for t in range(0,len(temp)):
        input("Schaumstoff vor Boson für FFC und Enter drücke")
        camera.do_ffc()
        input("Schaumstoff entfernen, SKS auf "+str(temp[t])+" Grad einstellen und Enter drücken")
        for i in range(0,420):
            print('Noch '+ str(420-i)+' s warten',end="\n")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        image=[]
        for p in range (0,100):
            image.append(camera.grab())
        print("Messung erfolgreich")
        np.save('temp'+str(temp[t]),image)