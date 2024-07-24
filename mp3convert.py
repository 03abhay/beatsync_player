from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import *
from pytube import YouTube
import requests
import moviepy.editor as editor
from PIL import Image , ImageTk
import homepage
class window5:
    def __init__(self):
        self.root= Tk()
       
        photo = PhotoImage(file = 'project_images/tklogo.png')
        self.root.iconphoto(False, photo)
        self.root.title("BeatSYNC MP3 Player")
        self.root.geometry("900x600")
        self.root.resizable(0,0)

        bgimg = Image.open('project_images\pink-guitar-with-white-musical-notes.jpg')
        image=bgimg.resize((900,600))
        pic=ImageTk.PhotoImage(image)
        piclable=Label(self.root,image=pic)
        piclable.place(x=0,y=0)

        self.lbl=Label(self.root,text="Enter URL",font=('arial',20))
        self.lbl.place(x=400, y=100, width=200, height=100)
        self.lbl.config(background='#ebc28e',foreground='black')

        self.ent=Entry(self.root)
        self.ent.place(x=400, y=170, width=300, height=30)
       
        self.btn=Button(self.root, text="DOWNLOAD", command=self.do)
        self.btn.place(x=500, y=220)


        homeimg = Image.open('project_images/homebutton.png')
        img1 = homeimg.resize((40,30))
        imga=ImageTk.PhotoImage(img1)
        self.backBtn = Button(self.root,image=imga,text='Back',compound=TOP,command = self.backcmd)
        self.backBtn.place(x = 4, y = 5)  

        self.root.mainloop()

    def backcmd(self):
        self.root.destroy()
        homepage.window2()
    def do(self):
        try:
            yt = YouTube(self.ent.get())
            data=yt.streaming_data
            print(yt.title)
            lst=[]
            for i in data['formats']:
                # print(i)
                if i['qualityLabel']=='720p':
                    lst.append(i['url'])
            print(lst)
            url=lst[0]
            headers = {'Content-Type':'application/json', 'x-app-id':'cf603149', 'x-app-key':'cbbd0d41f6db22ef430c149072faa50a'}
            res=requests.get(url,headers)
            # print(res.content)
            mp4=[('MP4 (Video)', '.mp4')]
            fl=filedialog.asksaveasfile(initialfile=yt.title, filetypes=mp4)
            fl1=yt.title
            # print(fl.name)
            with open(fl.name+'.mp4','wb') as file:
                file.write(res.content)
            namee=str(yt.title).split(" ")[:3]
            new_file = open('music/'+" ".join(namee)+'.mp3','wb')
            print(new_file)
            
            mp3file=editor.VideoFileClip(fl.name+'.mp4')
            mp3file.audio.write_audiofile('music/'+" ".join(namee)+'.mp3')
            mp3file.close()
            messagebox.showinfo("Success", "Song saved in music folder")
            self.root.destroy()
            homepage.window2()
        except Exception as e:
            print(e)
            messagebox.showerror('Alert', e)
if __name__ == "__main__":
     window5()        
