import pygame
import tkinter as tkr
from mutagen.mp3 import MP3
import os
from ttkthemes import themed_tk

player=themed_tk.ThemedTk()
player.get_themes()
player.set_theme('plastik')
player.title("Music Player")
player.iconbitmap(r"music.ico")
#player.configure(bg='#646160')
#player.geometry("400x400")

MUTE=False

os.chdir("D:/playlis")
songlist=os.listdir()


playlist=tkr.Listbox(player, highlightcolor='#646160',selectmode=tkr.SINGLE,bg='#A29F9E')

for i in songlist:
    pos =0
    playlist.insert(pos, i)
    pos+=1


pygame.init()
pygame.mixer.init()
i="n"
def play():

    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
    TimeInfo()
    i="n"
    return i

def Exit():
    pygame.mixer.music.stop()

def pause():
    global i
    if(i=='y'):
        pygame.mixer.music.unpause()
        
        i="n"
        
    elif(pygame.mixer.music.get_busy()):
        pygame.mixer.music.pause()
       
        i='y'

def loop():
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play(-1)
    
 
def TimeInfo():
      
      audio=MP3(playlist.get(tkr.ACTIVE) )
      totalLength=audio.info.length
      mins,sec=divmod(totalLength,60)
      mins=round(mins)
      sec=round(sec)
      timeFor ='{:02d}:{:02d}'.format(mins,sec)
      content2['text'] ="Total Length" + ' - ' +timeFor


def volumeCon(val):
    global MUTE
    if MUTE:
        pass
    else:
        
        vol=float(val)/100
        pygame.mixer.music.set_volume(vol)

def mute():
    global MUTE
    if MUTE:
        button5.configure(image=photospeaker)
        c=volume.get()
        print(c)
        vol=float(c)/100
        pygame.mixer.music.set_volume(vol)
        MUTE=False
    else:
        button5.configure(image=photomute)
        pygame.mixer.music.set_volume(0)
        MUTE=True
s=tkr.ttk.Style()
s.configure('new.TFrame',background='#646160')     
    
middleframe=tkr.ttk.Frame(player)

bottomframe=tkr.ttk.Frame(player)

volume=tkr.ttk.Scale(bottomframe,from_=0, to_=100, orient=tkr.HORIZONTAL,command=volumeCon)
volume.set(70) 
pygame.mixer.music.set_volume(0.7)     
photomute=tkr.PhotoImage(file='C:/Users\ASUS\music player\mute.png')
photospeaker=tkr.PhotoImage(file='C:/Users\ASUS\music player\speaker.png')
photoplay= tkr.PhotoImage(file='C:/Users\ASUS\music player\play.png')
photopause= tkr.PhotoImage(file='C:/Users\ASUS\music player\pause.png')
photostop= tkr.PhotoImage(file='C:/Users\ASUS\music player\stop.png')
photoloop= tkr.PhotoImage(file='C:/Users\ASUS\music player\loop.png')


button1=tkr.ttk.Button(middleframe,image=photoplay,command=play)
button2=tkr.ttk.Button(middleframe,image=photostop,command=Exit)
button3=tkr.ttk.Button(middleframe,image=photopause,command=pause)
button4=tkr.ttk.Button(bottomframe,image=photoloop,command=loop)
button5=tkr.ttk.Button(bottomframe,image=photospeaker,command=mute)
var=tkr.StringVar()
content1 =tkr.ttk.Label(player,textvariable=var)
content2=tkr.ttk.Label(player,text='Total Length : --:--')


'''packs'''
content1.pack()
playlist.pack(fill='both')
content2.pack(pady=10)
middleframe.pack(padx=25,pady=10)
bottomframe.pack(pady=10)
button1.pack(side="left",padx=10)
button2.pack(side="left",padx=10)
button3.pack(side="left",padx=10)
#button4.pack(side="left",padx=10)
button5.pack(side="left",padx=10)
volume.pack(side="left")
playlist.pack(fill='both')
button4.pack(side="left",padx=10)
player.mainloop()