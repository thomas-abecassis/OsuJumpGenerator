from tkinter import *
import datetime
import time
import pyautogui

###TKINTER###
fenetre = Tk()

canvas = Canvas(fenetre, width=1000, height=1000, background='white')
canvas.pack()



###TKINTER###


global micropasse,avant

micropasse=0
temps=datetime.datetime.now()
avant=temps.hour*3600000000+temps.minute*60000000+temps.second*1000000+temps.microsecond

def game(map):
    micropasse=0
    indexCercle=0
    cercleASuprimer=[]
    cercleTkinterASupprimer=[]
    while(True):
            time.sleep(0.033)
            micropasse+=tempsEntreFrame(micropasse)
            cercleCourant=map.getCercle(indexCercle)
            if(cercleCourant.getMicro()<micropasse):
                ##if(indexCercle<10000):
                   ## pyautogui.moveTo(400+cercleCourant.x*3.4, cercleCourant.y *4 + 50)
                print(map.PJ(indexCercle))
                cercleASuprimer.insert(0,cercleCourant)
                if (map.jumps.estContenu(cercleCourant)):
                    cercleTkinterASupprimer.insert(0,canvas.create_oval(cercleCourant.x*2,cercleCourant.y*2,cercleCourant.x*2+100,cercleCourant.y*2+100,width=2,outline="red"))
                else :
                    cercleTkinterASupprimer.insert(0,canvas.create_oval(cercleCourant.x*2,cercleCourant.y*2,cercleCourant.x*2+100,cercleCourant.y*2+100,width=2,outline="black"))                    
                indexCercle+=1
            if(len(cercleTkinterASupprimer)!=0 and micropasse-cercleASuprimer[len(cercleASuprimer)-1].getMicro()>200000):
                canvas.delete(cercleTkinterASupprimer[len(cercleTkinterASupprimer)-1])
                del cercleASuprimer[len(cercleASuprimer)-1]
                del cercleTkinterASupprimer[len(cercleTkinterASupprimer)-1]
            fenetre.update_idletasks()
            fenetre.update()
            
            
            
            
def tempsEntreFrame(micropasse):
    global avant 
    temps=datetime.datetime.now()
    mtn=temps.hour*3600000000+temps.minute*60000000+temps.second*1000000+temps.microsecond
    micropasse=mtn-avant
    avant=mtn
    return micropasse


    




