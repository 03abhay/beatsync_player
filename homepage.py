from tkinter import *
from tkinter.ttk import *
from PIL import Image , ImageTk
from pygame import mixer
import pygame,os
from tkinter import filedialog
import os

import mp3convert
import settings
import profilebtn   

pygame.mixer.init()
paused = False

class window2:
    def __init__(self):
        self.root= Tk()
       
        photo = PhotoImage(file = 'project_images/tklogo.png')
        self.root.iconphoto(False, photo)
        self.root.title("BeatSYNC Music Player")
        self.root.geometry("1000x600")
        self.root.resizable(0,0)
        
        canvas= Canvas(self.root, bd=2, highlightthickness=2)
        canvas.pack(side=TOP, padx=10, pady=10)

        
        # frames
        
        self.frame1 = Frame(self.root, width=500, height=600)
        self.loginimage = Image.open('project_images\image.jpg').resize((500,600))
        self.loginimageTk = ImageTk.PhotoImage(self.loginimage)
        self.imgLbl = Label(self.frame1, image = self.loginimageTk)
        self.imgLbl.place(x = 0, y = 0) 
        self.frame1.place(x = 0, y =0)
        
        self.frame2 = Frame(self.frame1,width=350, height=500)
        self.frame2.place(x = 80, y =50)

        self.frame3 = Frame(self.root,width=500, height=600)
        self.frame3.place(x=500,y=0)
        
        bgimg=Image.open('project_images\music-arrangement-with-black-headphones-cables.jpg')
        image_b=bgimg.resize((500,600))
        pic=ImageTk.PhotoImage(image_b)
        bgimg_lbl=Label(self.frame2,image=pic)
        bgimg_lbl.place(x =-70,y=-70)

        
        self.songs_list=Listbox(self.frame3,selectmode=SINGLE,bg="black",fg="white",font=('arial',10),height=100,width=500,selectbackground="gray",selectforeground="black")
        self.songs_list.grid(columnspan=10)
        self.songs_list.place(x=0,y=50)
        temp_song=os.listdir(os.path.abspath('music'))
        for s in temp_song:
            s=os.path.abspath('music/'+s)
            self.songs_list.insert(END,s)
       

# buttons
       
        
       
        
        playimg=Image.open('project_images\play_btn.png')
        img1 = playimg.resize((45,45))
        imga= ImageTk.PhotoImage(img1)
        self.playbtn = Button(self.frame2,image=imga,text="p",command=self.play) 
        self.playbtn.place(x=110,y=425)     
        
        pauseimg=Image.open('project_images\pause_8059599.png')
        img_1 = pauseimg.resize((45,45))
        imgage= ImageTk.PhotoImage(img_1)
        self.pausebtn = Button(self.frame2,image=imgage,command=self.pause) 
        self.pausebtn.place(x=170,y=425)
        
        ytimg=Image.open('project_images\youtube.png')
        img_yt=ytimg.resize((20,20))
        ytbtn=ImageTk.PhotoImage(img_yt)
        mp3toyt_btn=Button(self.frame3,image=ytbtn,text='mp3 CONVERTER',compound=TOP,command=self.ytconvertercmd)
        # mp3toyt_btn.config(bg='#d3e8f3')
        mp3toyt_btn.place(x=83,y=0)

        backimg=Image.open('project_images/back_btn.png')
        img2=backimg.resize((33,21))
        imgb=ImageTk.PhotoImage(img2)
        self.backbtn = Button(self.frame2,image=imgb,command=self.back) 
        self.backbtn.place(x=55,y=435)  

        nextimg=Image.open('project_images/next-btn.png')
        img3=nextimg.resize((33,21))
        imgc=ImageTk.PhotoImage(img3)
        self.nextbtn = Button(self.frame2,image=imgc,command=self.next) 
        self.nextbtn.place(x=239,y=435)  

       

        settingimg=Image.open('project_images/settings.png')
        img6=settingimg.resize((25,21))
        imgf=ImageTk.PhotoImage(img6)
        self.repeatbtn=Button(self.frame3,image=imgf,text='SETTINGS',compound=TOP ,command=self.settingscmd)
        self.repeatbtn.place(x=195,y=0)
        
        addmusic = Image.open('project_images/folder_5430797.png')
        img7 =addmusic.resize((25,20))     
        imgg=ImageTk.PhotoImage(img7)
        self.addfolder_btn=Button(self.frame3,image=imgg,text='ADD music',compound=TOP,command=self.add)
        self.addfolder_btn.place(x=0,y=0)
        
        
        
        
        self.root.mainloop()

# menu buttons
    
  
   
    def ytconvertercmd(self):
        self.root.destroy()
        mp3convert.window5()
    
    def settingscmd(self):
        self.root.destroy()
        settings.window7()


# buton declaration
    def add(self):

        
        temp_song=filedialog.askopenfilenames(title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
        for s in temp_song:
            s=s.replace("","")
            self.songs_list.insert(END,s)

    def play(self):
               
        Music_Name = self.songs_list.get(ACTIVE)
        print(Music_Name[0:-4])
        mixer.music.load(self.songs_list.get(ACTIVE))
        mixer.music.play()

       
    def pause(self):
        global paused
        if paused == True:
            pygame.mixer.music.unpause()
            paused = False
        elif paused == False:
            pygame.mixer.music.pause()
            paused = True
    
    def back(self):
        previous_one=self.songs_list.curselection()

        previous_one=previous_one[0]-1

        temp2=self.songs_list.get(previous_one)
        temp2=f'{temp2}'
        mixer.music.load(temp2)
        mixer.music.play()
        self.songs_list.selection_clear(0,END)

        self.songs_list.activate(previous_one)
        self.songs_list.selection_set(previous_one)
    
    
    def next(self):
        next_one=self.songs_list.curselection()
        next_one=next_one[0]+1
        temp=self.songs_list.get(next_one)
        temp=f'{temp}'
        mixer.music.load(temp)
        mixer.music.play()
        self.songs_list.selection_clear(0,END)
        self.songs_list.activate(next_one)
        self.songs_list.selection_set(next_one)
    
   
    def settings(self):
        
         self.root.destroy()
         settings.window7()


if __name__ == "__main__":
    window2()        