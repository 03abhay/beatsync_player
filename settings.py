from tkinter import *
from tkinter.ttk import *
from PIL import Image , ImageTk
import homepage
import loginWindow
class window7:
    def __init__(self):
        self.root= Tk()
       
        photo = PhotoImage(file = 'project_images/tklogo.png')
        self.root.iconphoto(False, photo)
        self.root.title("BeatSYNC MP3 Player")
        self.root.geometry("900x600")
        self.root.resizable(0,0)

        homebgimg = Image.open('project_images\copy-space-headphones-laptop-air-concept.jpg')
        img_1 = homebgimg.resize((900,600))
        img_a=ImageTk.PhotoImage(img_1)      
        bg_lbl=Label(self.root,image=img_a)
        bg_lbl.place(x=0,y=0)

        homeimg = Image.open('project_images/homebutton.png')
        img1 = homeimg.resize((40,30))
        imga=ImageTk.PhotoImage(img1)
        self.backBtn = Button(self.root,image=imga, text='BACK',compound=TOP,command = self.back)
        self.backBtn.place(x = 10, y = 10)  

        img = Image.open('project_images\power_9068818.png')
        img3 = img.resize((150,140))
        imgb=ImageTk.PhotoImage(img3)
        self.backBtn = Button(self.root,image=imgb,text='LOGOUT',compound=TOP, command = self.logout)
        self.backBtn.place(x = 180, y = 400) 

        self.root.mainloop()    

    def back(self):
        self.root.destroy()
        homepage.window2()
    def logout(self):
        
        self.root.destroy()
        loginWindow.window1()



if __name__ == "__main__":
    window7()      