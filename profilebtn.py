from tkinter import *
from tkinter.ttk import *
from PIL import Image , ImageTk
import homepage
import new_register
class window8:
    def __init__(self):
        self.root= Tk()
       
        photo = PhotoImage(file = 'project_images/tklogo.png')
        self.root.iconphoto(False, photo)
        self.root.title("BeatSYNC MP3 Player")
        self.root.geometry("900x600")
        self.root.resizable(0,0)
        
        
        homebgimg = Image.open('project_images\guitarist-playing-stage-illuminated-by-spotlight-generated-by-ai.jpg')
        img_1 = homebgimg.resize((900,600))
        img_a=ImageTk.PhotoImage(img_1)      
        bg_lbl=Label(self.root,image=img_a)
        bg_lbl.place(x=0,y=0)
        homeimg = Image.open('project_images/homebutton.png')
        img1 = homeimg.resize((40,30))
        imga=ImageTk.PhotoImage(img1)
        self.backBtn = Button(self.root,image=imga, text='Back',compound=TOP,command = self.back)
        self.backBtn.place(x = 10, y = 0)  

       

        
        bgimg=Image.open("project_images/vinyl_7085136.png")
        img2 = bgimg.resize((240,230))
        imgb=ImageTk.PhotoImage(img2)
        self.backBtn = Button(self.root,image=imgb,text='PROFILE',compound=TOP ,command = self.home)
        self.backBtn.place(x = 500, y = 100)  



        self.root.mainloop()    

    def back(self):
        self.root.destroy()
        homepage.window2()

    def home(self):
        self.root.destroy()
        new_register.window9()

if __name__ == "__main__":
    window8()      