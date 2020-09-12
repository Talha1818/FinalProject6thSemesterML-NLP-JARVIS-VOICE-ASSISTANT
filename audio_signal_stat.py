from tkinter import *
from PIL import Image,ImageTk
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc

class audio_stat(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.maxsize(800, 600)
        self.title("Audio Signal | Statistics")
        self.frquency_sampling, self.audio_signal = wavfile.read("user.wav")
        self.audio_duration = round(self.audio_signal.shape[0] / float(self.frquency_sampling), 2)
        self.features_mfcc = mfcc(self.audio_signal, self.frquency_sampling)
        self.no_of_windows = self.features_mfcc.shape[0]
        self.length_of_each_feature = self.features_mfcc.shape[1]

    def add_background(self):
        self.image = Image.open("images/aud.jpg")
        self.image = self.image.resize((800, 600), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)
        self.li = Button(image = self.img)
        self.li.image = self.img
        self.li.pack()
    def audio_data(self):

        print(self.frquency_sampling)
        print(self.audio_signal)
        print("Audio Signal Shape : ", self.audio_signal.shape)
        print("Audio Signal Dtype : ", self.audio_signal.dtype)


        print("Audio Signal Duration : ", self.audio_duration," seconds")

        self.l1 = Label(text="Frequency Sampling -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l1.place(x=130, y=40)
        self.l2 = Label(text="Audio Signal -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l2.place(x=130, y=100)
        self.l3 = Label(text="Audio Signal Shape -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l3.place(x=130, y=160)
        self.l4 = Label(text="Audio Signal Dtype -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l4.place(x=130, y=220)
        self.l5 = Label(text="Audio Signal Duration -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l5.place(x=130, y=280)
        self.l5 = Label(text="Number of Windows mfcc -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l5.place(x=130, y=340)
        self.l5 = Label(text="Length of each Feature -->", padx=20, pady=12, font="courier 12 bold", bg="red",
                        fg="white", borderwidth=4, relief=SUNKEN)
        self.l5.place(x=130, y=400)


        self.l5 = Label(text=f"{self.frquency_sampling}", padx=20, pady=12, font="courier 12 bold",
                         borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l5.place(x=450, y=40)
        self.l6 = Label(text=f"{self.audio_signal}", padx=20, pady=12, font="courier 12 bold",
                        borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l6.place(x=450, y=100)
        self.l7 = Label(text=f"{self.audio_signal.shape}", padx=20, pady=12, font="courier 12 bold",
                        borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l7.place(x=450, y=160)
        self.l8 = Label(text=f"{self.audio_signal.dtype}", padx=20, pady=12, font="courier 12 bold",
                        borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l8.place(x=450, y=220)
        self.l8 = Label(text=f"{self.audio_duration} seconds", padx=20, pady=12, font="courier 12 bold",
                        borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l8.place(x=450, y=280)
        self.l8 = Label(text=f"{self.no_of_windows}", padx=20, pady=12, font="courier 12 bold",
                        borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l8.place(x=450, y=340)
        self.l8 = Label(text=f"{self.length_of_each_feature}", padx=20, pady=12, font="courier 12 bold",
                        borderwidth=4, relief=SUNKEN,bg="black",fg="white")
        self.l8.place(x=450, y=400)

        self.b1 = Button(text="Audio Signal Graph",command=self.graph, bg="black",fg="white",padx=20, pady=12, borderwidth=5,font="courier 20 bold", relief=SUNKEN)
        self.b1.place(x=60, y=500)

        self.b1 = Button(text="Audio Signal mfcc", command=self.graph_mfcc, bg="black", fg="white", padx=20, pady=12,
                         borderwidth=5, font="courier 20 bold", relief=SUNKEN)
        self.b1.place(x=440, y=500)

    def graph(self):
        self.audio_signal = self.audio_signal / np.power(2, 15)
        self.signal = self.audio_signal[:5000]
        time_axis = 1000 * np.arange(0, len(self.signal), 1) / float(self.frquency_sampling)
        plt.plot(time_axis, self.signal, color="red")
        plt.xlabel("Time(miliseconds)")
        plt.ylabel("Amplitude")
        plt.title("Input Audio Signal")
        plt.show()
    def graph_mfcc(self):

        print("Number of Windows : ",self.no_of_windows )
        print("Length of each Features  : ", self.length_of_each_feature)
        plt.matshow(self.features_mfcc.T)
        plt.title("MFCC")
        plt.show()









if __name__ == '__main__':
    stat = audio_stat()
    stat.add_background()
    stat.audio_data()
    mainloop()
    