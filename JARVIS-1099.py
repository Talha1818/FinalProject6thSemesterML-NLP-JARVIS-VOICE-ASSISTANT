from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import audio_signal_stat
import tkinter.messagebox as msg
import time

class JARVIS(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.maxsize(800,600)
        self.title("JARVIS")
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')

        self.voice = self.engine.setProperty('voice', self.voices[0].id)


    def add_background(self):
        self.image = Image.open("images/jar1.png")
        self.image = self.image.resize((800, 600), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.li = Button(image = self.img, text="TALHA")
        self.li.image = self.img
        self.li.pack()
        self.Menubar()

    def Menubar(self):
        self.menubar = Menu()
        self.menuitems = Menu(self.menubar, tearoff=0,bg="red",fg="white")
        self.menuitems.add_command(label="Youtube", command=self.youtube)
        self.menuitems.add_separator()
        self.menuitems.add_command(label="Google", command=self.google)
        self.menuitems.add_separator()
        self.menuitems.add_command(label="PhpStorm", command=self.php)
        self.menuitems.add_separator()
        self.menuitems.add_command(label="Play Music", command=self.play_music)

        self.menuitems_stat = Menu(self.menubar, tearoff=0,bg="red",fg="white")
        self.menuitems_stat.add_command(label="Audio Signal Statistics", command=self.audio_stat)

        self.menubar.add_cascade(label="Open", menu=self.menuitems)
        self.menubar.add_cascade(label="Statistics", menu=self.menuitems_stat)
        self.menubar.add_cascade(label="Exit", command=quit)
        self.config(menu=self.menubar)


    def add_audio_button(self):
        self.image = Image.open("images/rec1.png")
        self.image = self.image.resize((52, 53), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.b1 = Button(image=self.img, command=self.wishMe, bg="red",borderwidth=3, relief =SUNKEN)
        self.b1.place(x=480,y=40)

        self.l2 = Label(text="Say Something on MIC -->", padx=20,pady=13,font = "courier 15 bold",bg="red",fg="white",borderwidth=4, relief =SUNKEN)
        self.l2.place(x=124,y=40)

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
    def speak_to_sav_audio_file(self,save_audio):
        self.engine.save_to_file(save_audio, filename='user.wav', name='TALHA')
        self.engine.runAndWait()

    def wishMe(self):
        self.hours = int(datetime.datetime.now().hour)
        if self.hours >= 0 and self.hours < 12:
            self.speak("GOOD MORNING TALHA")
        elif self.hours >= 12 and self.hours < 18:
            self.speak("GOOD AFTERNOON TALHA")
        else:
            self.speak("GOOD EVENING TALHA")
        self.speak("I am a JARVIS TALHA ! Plz TELL ME HOW MAY I HELP YOU?")
        self.user_query()
    def status_barr(self):
        self.status_bar = StringVar()
        self.status_bar.set("Ready")
        self.l2 = Label(textvariable=self.status_bar, relief=SUNKEN, anchor=W,font = "courier 15 bold",bg="red",fg="white",borderwidth=4)
        self.l2.place(x=0,y=565,width=800)

    def takeCommand(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as self.source:
            print("Listening....")
            self.status_bar.set("Listening....please wait a little bit !")
            # msg.showinfo("JARVIS","Listening....")
            self.l2.update()
            self.r.pause_threshold = 1
            self.audio = self.r.listen(self.source)

        try:
            print("Recognizing...")
            self.status_bar.set("Recognizing....Your query will be ready after few seconds !")
            # msg.showinfo("JARVIS", "Recognizing....")
            self.l2.update()
            self.query = self.r.recognize_google(self.audio, language="en-in")
            self.status_bar.set("Ready")
            print(f"User Said : {self.query}\n")
            self.speak("User Say that : ")
            self.speak(self.query)
            # self.speak_to_sav_audio_file(self.query)

        except Exception as e:
            print("Please Say Something Again!")
            # self.speak("Please Say Something Again!")
            return "None"
        return self.query

    def user_query(self):
        self.query = self.takeCommand().lower()

        # logic to executing task based on query
        if 'wikipedia' in self.query:
            self.speak("Searching Wikipedia...")
            self.query = self.query.replace("wekipedia", "")
            self.results = wikipedia.summary(self.query, sentences=2)
            print(self.results)
            self.speak(self.results)
        elif 'open youtube' in self.query:
            self.youtube()
        elif 'open google' in self.query:
            self.google()
        elif 'play music' in self.query:
            self.play_music()
        elif 'time' in self.query:
            self.strtime = datetime.datetime.now().strftime('%H:%M:%S')
            print(self.strtime)
            self.speak(f"Now The Time is : {self.strtime}")
        elif 'open php' in self.query:
            self.php()
        elif 'email to ali' in self.query:
            try:
                self.speak("Hi Talha! please convey your message.")
                self.message = self.takeCommand()
                self.speak_to_sav_audio_file(self.message)
                self.receiver = [["muhammadtalha1818@gmail.com"], ["muhammadtalha181818@gmail.com"]]
                # to = ["muhammadtalha1818@gmail.com"]
                self.send_email(self.receiver, self.message)
                self.l2.update()
                self.status_bar.set("Ready.. Your email has been sent successfully!")
                self.speak("Your email has been sent successfully!")
            except Exception as e:
                self.speak("Email has not been sent ! Something went Wrong !")
        elif "quit" in self.query:
            exit()

    def youtube(self):
        webbrowser.open('youtube.com')
        self.speak("Mr Talha ! youtube has been opened ... please check it")
    def google(self):
        webbrowser.open('google.com')
        self.speak("Mr Talha ! google has been opened ... please check it")
    def play_music(self):
        songs_dir = "F:\\Movies\\songs"
        songs = os.listdir(songs_dir)
        # print(songs)
        os.startfile(os.path.join(songs_dir, songs[3]))
        self.speak("Mr Talha ! Music has been started ... please feel it")
    def php(self):
        path = "C:\\Program Files\\JetBrains\\PhpStorm 2019.3.3\\bin\phpstorm64.exe"
        os.startfile(path)
        self.speak("Mr Talha ! phpstorm has been opened ... please check it")
    def audio_stat(self):
        self.destroy()
        aud = audio_signal_stat.audio_stat()
        aud.add_background()
        aud.audio_data()

    def send_email(self,receiver,message):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        from_= 'muhammadtalha1818@gmail.com'

        self.server.ehlo()
        self.server.starttls()
        self.server.login('muhammadtalha1818@gmail.com', 'viratkohli')
        self.server.sendmail(from_, receiver,message)
        self.server.close()
        # lfxsojiluacdxucs

    def clock(self):
        self.label = Label( font=("courier", 40, 'bold'), bg="black", fg="red")
        self.label.place(x=200, y=270,width=400)
        self.text_input = time.strftime("%H:%M:%S")
        self.label.config(text=self.text_input)
        self.label.after(200, self.clock)








if __name__ == '__main__':
    jar = JARVIS()
    jar.add_background()
    jar.add_audio_button()
    jar.status_barr()
    jar.clock()
    jar.mainloop()