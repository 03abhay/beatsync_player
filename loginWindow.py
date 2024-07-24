from tkinter import *
from PIL import Image
from webbrowser import BackgroundBrowser
from PIL import Image , ImageTk
from tkinter import messagebox

import homepage
import new_register,database

class window1:
    def __init__(self):
        self.root= Tk()
       
        
        photo = PhotoImage(file = 'project_images/tklogo.png')
        self.root.iconphoto(False, photo)
        self.root.title("BeatSYNC MP3 Player")
        self.root.geometry("900x600")
        self.root.resizable(0,0)

        canvas= Canvas(self.root, bd=2, highlightthickness=2)
        canvas.pack(side=TOP, padx=10, pady=10)

        
        pic=Image.open("project_images\Screenshot (2).png").resize((950,600))
        bg = ImageTk.PhotoImage(pic)
        self.Labelimg =Label(self.root,image=bg)
        self.Labelimg.place(x=0,y=0) 
        
        self.frame2 = Frame(self.root, width=390, height=500)
        self.frame2.place(x = 470, y = 65)
         
   
        
        self.frame2.config(bg="#000321") 
        self.welcome_label = Label(self.root, text = ' Dive in music',fg="#03dffc",bg='#000321')
        self.welcome_label.config(font=("harlow solid italic",30,))
        self.welcome_label.place(x=545,y=30)

        
        userimg = Image.open('project_images/user_8679899.png')
        userimg1 = userimg.resize((90,90))
        imgg2 = ImageTk.PhotoImage(userimg1)
        
        self.userimg_label=Label(self.frame2,image=imgg2,bg="#000321")
        self.userimg_label.place(x=140, y=60)

        self.firstLbl = Label(self.frame2, text = 'User - Name', fg = 'white',bg='#000321', font = ('harlow solid italic', 20), wraplength=400, justify='left')
        self.firstLbl.place(x = 115, y = 155)
        self.userEntry = Entry(self.frame2,width=40)
        self.userEntry.configure(bg='#d3e8f3')
        self.userEntry.place(x = 60, y = 195)

        self.firstLbl = Label(self.frame2, text = 'Password', fg = 'white',bg='#000321', font = ('harlow solid italic', 20), wraplength=400, justify='left')
        self.firstLbl.place(x = 135, y = 225)
        self.userEntry1 = Entry(self.frame2, show='♪',width=40)
        self.userEntry1.configure(bg='#d3e8f3')
        self.userEntry1.place(x = 60, y = 265)

        self.firstLb2 = Label(self.frame2, text = 'New User ', fg = 'white', bg='#000321',font = ('Britannic Bold', 15), wraplength=400, justify='left')
        self.firstLb2.place(x = 8, y = 410)
        
        
        loginimg = Image.open('project_images\login-button-png-18022.png')
        img1=loginimg.resize((100,50)) 
        imga=ImageTk.PhotoImage(img1)
        
        self.loginBtn1 = Button(self.frame2,image=imga,borderwidth=0, command = self.loginUser)
        self.loginBtn1.configure(bg="#000321")
        self.loginBtn1.place(x = 140, y =300)
       
        
        skipimg = Image.open('project_images/next-btn.png')
        skip=skipimg.resize((30,20))
        Labeimg =ImageTk.PhotoImage(skip)
        self.loginBtn2 = Button(self.frame2, image=Labeimg,text = "SKIP",compound=RIGHT,fg='white',borderwidth=0 ,command = self.skipLogin)
        self.loginBtn2.configure(bg="#000321")
        self.loginBtn2.place(x = 310 ,y = 475)
       
        registerimg = Image.open('project_images/register.png')
        img2 = registerimg.resize((70,25))
        imgb = ImageTk.PhotoImage(img2)
        self.loginBtn3 = Button(self.frame2, text = "click her to ", image=imgb,borderwidth=0, fg='white',command = self.register)
        self.loginBtn3.configure(bg="#000321")
        self.loginBtn3.place(x = 103, y = 410)

        


        
        self.root.mainloop()
    
    def loginUser(self):
        uname=self.userEntry.get()
        upass=self.userEntry1.get()
        data=(uname,upass)
        get_data=database.loginUser(data)
        if get_data:
               self.root.destroy()
               homepage.window2()
        else:
               messagebox.showerror('Authentication Failed','User not found')
    def skipLogin(self):
                self.root.destroy()
                homepage.window2()
    def register(self):
                self.root.destroy()
                new_register.window9()

if __name__ == '__main__':
    
    window1() 



