from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
import database,loginWindow
class window9:
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

        regimg = Image.open('project_images/verify_2921147.png').resize((70,50))
        img_1=ImageTk.PhotoImage(regimg)
        self.regimglbl = Label(self.frame2,image=img_1,bg="#000321")
        self.regimglbl.place(x=80,y=10)
        self.welcome_label = Label(self.frame2, text = 'SIGN UP',fg="#03dffc",bg='#000321')
        self.welcome_label.config(font=("Myriad Pro Cond",20))
        self.welcome_label.place(x=160,y=15)
        
        self.lbl1 = Label(self.frame2,text= 'USERNAME',font='arial',bg="#000321",fg='white')
        self.lbl1.place(x=5,y=110)
        self.userEntry1 = Entry(self.frame2,width=50)
        self.userEntry1.configure(bg='#d3e8f3')
        self.userEntry1.place(x = 155, y = 113)
        
        self.lbl1 = Label(self.frame2,text= 'USERNAME',font='arial',bg="#000321",fg='white')
        self.lbl1.place(x=5,y=110)
        self.userEntry1 = Entry(self.frame2,width=50)
        self.userEntry1.configure(bg='#d3e8f3')
        self.userEntry1.place(x = 155, y = 113)

        self.lbl2 = Label(self.frame2,text= 'E-mail ID',font='arial',bg="#000321",fg='white')
        self.lbl2.place(x=5,y=150)
        self.userEntry2 = Entry(self.frame2,width=50)
        self.userEntry2.configure(bg='#d3e8f3')
        self.userEntry2.place(x = 155, y = 153)

        self.lbl3 = Label(self.frame2,text= 'NEW PASSWORD',font='arial',bg="#000321",fg='white')
        self.lbl3.place(x=5,y=230)
        self.userEntry3 = Entry(self.frame2,width=40)
        self.userEntry3.config(bg='#d3e8f3')
        self.userEntry3.place(x = 50, y = 270)

        self.lbl4= Label(self.frame2,text= 'CONFIRM PASSWORD',font='arial',bg="#000321",fg='white')
        self.lbl4.place(x=5,y=300)
        self.userEntry4 = Entry(self.frame2,width=40)
        self.userEntry4.config(bg='#d3e8f3')
        self.userEntry4.place(x = 50, y = 340)
        


        btnimg = Image.open('project_images/right-arrow_1359245.png').resize((50,50))
        # btnimg.c(bg='#000321')
        img_2 = ImageTk.PhotoImage(btnimg)

        submit_btn = Button(self.frame2,text='submit',image=img_2,fg='white',borderwidth=0,compound=TOP,command=self.submitcmd)
        submit_btn.config(bg='#000321')
        submit_btn.place(x = 140, y = 420)
        
        self.root.mainloop()

    def submitcmd(self):
        uname=self.userEntry1.get()
        umail=self.userEntry2.get()
        upass=self.userEntry3.get()
        data=(uname,upass,umail)
        if self.userEntry3.get()==self.userEntry4.get():
            get_data=database.registerUser(data)
            if get_data:
                messagebox.showinfo('Success', 'User Registered')
                self.root.destroy()
                loginWindow.window1()
            else:
                messagebox.showerror('Authentication Failed','User not found')
        else:
            messagebox.showwarning("Attention","Password doesn't match")

if __name__ == '__main__':
    window9()        