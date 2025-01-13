import json
import os
import random
import sys
import time
import tkinter.ttk
from datetime import datetime
from tkinter import *
from tkinter import PhotoImage

import pyttsx3
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr


class CELPIPTest:
    def __init__(self, master):
        self.master = master
        self.master.title("CELPIP Test")
        self.master.geometry("300x300")
        self.jData = self.getJson()
        self.sec1 = StringVar()
        self.sec2 = StringVar()
        self.Q = StringVar()
        self.WW = StringVar()
        self.T = StringVar()
        self.L = StringVar()
        self.ss = StringVar()
        self.ff = StringVar()
        self.bb = StringVar()
        self.var = IntVar()
        self.timer = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.imagePath = StringVar()
        self.testtime = datetime.now().strftime("%d_%m")
        self.testhourmin = datetime.now().strftime('%H_%M')
        self.startfrom = 0
        self.TT = Text(self.master, height=35, width=85, font='Helvetica14')
        self.PT = Label(self.master, text="Prep-time remaining: ", font='Helvetica14', justify=LEFT)
        self.PTE = Entry(self.master, textvariable=self.sec1, width=2, font='Helvetica14')
        self.RT = Label(self.master, textvariable=self.timer, font='Helvetica14')
        self.RTE = Entry(self.master, textvariable=self.sec2, width=2, font='Helvetica14')
        self.LL = Label(self.master, textvariable=self.L, font='Helvetica14', justify=LEFT)
        Label(self.master, textvariable=self.Q, font='Helvetica14', justify=LEFT).place(x=50, y=90)
        Label(self.master, textvariable=self.T, font='Helvetica14', justify=LEFT).place(x=50, y=30)
        self.WC = Label(self.master, textvariable=self.WW, font='Helvetica14', justify=LEFT)
        self.WW.set('Word-count: 0')
        self.ST = Button(self.master, textvariable=self.ss, command=self.on_click, width=20)
        self.ss.set("Start Test")
        self.FT = Button(self.master, textvariable=self.ff, command=self.finish, width=20)
        self.ff.set("Exit Test")
        self.BB = Button(master, textvariable=self.bb, command=self.callMainAgain, width=20)
        self.bb.set("Back to Test")

        self.ST.place(x=80, y=150)
        self.FT.place(x=80, y=180)

        self.can = Canvas(self.master, width=300, height=50)
        self.can.place(x=1, y=240)
        self.wd = os.getcwd()
        self.path = os.path.join(self.wd, "images/developerBy.png")
        self.image = PhotoImage(file=self.path)
        self.can.create_image(1, 50, anchor=SW, image=self.image)
        self.myProgBar = tkinter.ttk.Progressbar(self.master, orient=HORIZONTAL, length=700, mode='determinate')
        self.rad1 = Radiobutton(self.master, text="Option 1", variable=self.var, value=1)
        self.rad2 = Radiobutton(self.master, text="Option 2", variable=self.var, value=2)
        self.c1 = Checkbutton(self.master, text='WritingTask', variable=self.var1, onvalue='WritingTask', offvalue='', state="active")
        self.c1.place(x=80, y=10)
        self.c2 = Checkbutton(self.master, text='SpeakingTask', variable=self.var2, onvalue='SpeakingTask', offvalue='')
        self.c2.place(x=80, y=40)
        self.c3 = Checkbutton(self.master, text='ReadingTask', variable=self.var3, onvalue='ReadingTask', offvalue='')
        self.c3.place(x=80, y=70)
        self.c4 = Checkbutton(self.master, text='ListeningTask', variable=self.var4, onvalue='ListeningTask', offvalue='')
        self.c4.place(x=80, y=100)

    def create_master(self):
        self.master = Tk()
        self.__init__(self.master)
        self.master.mainloop()

    def getJson(self):
        with open("questions.json") as fp:
            qus = json.load(fp)
        return qus

    def prepCounter(self, preptime):
        preptime -= 1
        while preptime > -1:
            self.sec1.set(preptime)
            preptime -= 1
            self.master.update()
            time.sleep(1)

    def durationCounter(self, duration):
        duration -= 1
        temp = 0
        while duration > -1:
            self.sec2.set(duration)
            duration -= 1
            temp += 1
            self.master.update()
            total = duration + temp + 1
            print("%", ((total - duration) / total) * 100, "total", total, "duration", duration)
            self.progBarUpdate(((total - duration) / total) * 100)
            time.sleep(1)

    def durationCounterW(self, duration):
        temp = 0
        duration = duration * 60
        while duration > -0.5:
            self.sec2.set(int(duration / 60))
            duration -= 0.5
            temp += 0.5
            self.master.update()
            total = duration + temp
            print("%", ((total - duration) / total) * 100, "total", total, "mins", duration / 60)
            self.progBarUpdate(((total - duration) / total) * 100)
            self.WW.set('Word-count: %s' % len(self.TT.get('1.0', END).split(' ')))
            time.sleep(0.5)

    def Voice_rec(self, duration, name):
        engine = pyttsx3.init()
        text = "Please start speaking now"
        engine.say(text)
        engine.runAndWait()
        fs = 48000
        r = sr.Recognizer()
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        self.durationCounter(duration)
        self.progBarStop()
        self.Q.set("Please wait writing your audio file and audio to text file")
        self.master.update()
        sf.write(name, myrecording, fs)
        try:
            with sr.AudioFile(os.path.join(os.getcwd(), name)) as audio:
                data = r.record(audio)
                text = r.recognize_google(data)
                filename = name.replace('flac', 'txt')
                with open(filename, 'w') as file:
                    file.write(text)
        except:
            self.Q.set('Error in writing audio to text file')
            self.master.update()
            time.sleep(2)

    def setImage(self, path):
        self.image = PhotoImage(file=path)
        self.can.create_image(5, 400, anchor=SW, image=self.image)
        self.can.image = self.image

    def showRadiobutton(self):
        self.rad1.place(x=150, y=200)
        self.rad2.place(x=500, y=200)

    def destroyRadiobutton(self):
        self.rad1.destroy()
        self.rad2.destroy()

    def progBarUpdate(self, percVar):
        self.myProgBar['value'] = percVar
        self.master.update()

    def progBarStop(self):
        self.myProgBar.stop()

    def finish(self):
        self.master.destroy()

    def designForSpeakingTask(self):
        self.master.title("Speaking-Task")
        self.master.geometry("900x600")
        self.ST.destroy()
        self.can.place(x=5, y=550)
        self.var.set(1)
        self.PT.place(x=650, y=30)
        self.PTE.place(x=850, y=30)
        self.sec1.set('00')
        self.RT.place(x=650, y=60)
        self.RTE.place(x=850, y=60)
        self.sec2.set('00')
        self.myProgBar.place(x=100, y=5)
        self.ff.set("Close Test")
        self.FT.place(x=700, y=550)
        self.BB.place(x=80, y=210)
        self.timer.set("Record-time remaining: ")
        self.master.update()
        for ind in range(self.startfrom, 9):
            data = self.jData['SpeakingTask'][str(ind)]
            noOfQ = (len(data) - 3) if ind != 5 else (len(data) - 3) / 2
            self.T.set("Task:-%s : %s" % (ind, data['0']))
            self.master.update()
            randV = random.randrange(1, noOfQ + 1)
            duration = data['duration']
            preptime = data['preptime']
            qus = data[str(randV)]
            self.Q.set("Qus:- %s" % qus)
            self.master.update()
            if ind in (3, 4, 5, 8):
                currPath = os.path.join(os.getcwd(), "images/Task%s/%s.png" % (ind, randV))
                if ind == 5:
                    self.setImage(currPath)
                    self.showRadiobutton()
                    self.prepCounter(60)
                    currPath = os.path.join(os.getcwd(), "images/Task%s/%s_%s.png" % (ind, randV, self.var.get()))
                    self.destroyRadiobutton()
                    qus = data["%s_2" % randV]
                    self.Q.set("Q:- %s" % qus)
                self.setImage(currPath)
            self.prepCounter(preptime)
            name = "%s/S/%s_%s.flac" % (self.testtime, ind, self.testhourmin)
            self.Voice_rec(duration, name)
            self.setImage(self.path)
            self.Q.set("Qus:- ")

    def designForWritingTask(self):
        self.master.title("Writing-Task")
        self.master.geometry("900x900")
        self.master.resizable(False, False)
        self.ST.destroy()
        self.can.place(x=5, y=850)
        self.PT.place(x=650, y=30)
        self.PTE.place(x=850, y=30)
        self.sec1.set('00')
        self.RT.place(x=650, y=60)
        self.RTE.place(x=850, y=60)
        self.sec2.set('00')
        self.myProgBar.place(x=100, y=5)
        self.ff.set("Close Test")
        self.FT.place(x=700, y=860)
        self.BB.place(x=520, y=860)
        self.timer.set("Writing-time remaining: ")
        self.WC.place(x=380, y=860)
        self.TT.place(x=60, y=220)
        self.master.update()
        for ind in range(1, 3):
            data = self.jData['WritingTask'][str(ind)]
            noOfQ = len(data) - 3
            self.T.set("Task:-%s : %s" % (ind, data['0']))
            self.master.update()
            randV = random.randrange(1, noOfQ + 1)
            duration = data['duration']
            qus = data[str(randV)]
            self.Q.set("Qus:- %s" % qus)
            self.master.update()
            self.durationCounterW(duration)
            text = self.TT.get('1.0', END)
            name = "%s/W/%s_%s.txt" % (self.testtime, ind, self.testhourmin)
            self.writeTexttoFile(name, text)
            self.TT.delete('1.0', END)
            self.master.update()
        self.TT.destroy()
        self.WC.destroy()

    def writeTexttoFile(self, name, text):
        with open(name, 'w') as fp:
            fp.write(text)

    def createFolders(self):
        try:
            print(os.path.join(self.wd, f'{self.testtime}'))
            os.makedirs(os.path.join(self.wd, f'{self.testtime}\W'), exist_ok=True)
            os.makedirs(os.path.join(self.wd, f'{self.testtime}\S'), exist_ok=True)
            os.makedirs(os.path.join(self.wd, f'{self.testtime}\R'), exist_ok=True)
            os.makedirs(os.path.join(self.wd, f'{self.testtime}\L'), exist_ok=True)
        except:
            print('error')
            pass

    def callMainAgain(self):
        self.master.destroy()
        self.create_master()

    def on_click(self):
        self.createFolders()
        options = [self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get()]
        self.c1.destroy()
        self.c2.destroy()
        self.c3.destroy()
        self.c4.destroy()
        if self.var3.get() == 'ReadingTask' or self.var4.get() == 'ListeningTask':
            self.L.set('Module is still in development.\nYou can exit and start again for\nother modules')
            self.LL.place(x=55, y=60)
            self.ST.destroy()
            self.BB.place(x=80, y=210)
            self.master.update()
        else:
            for title in self.jData.keys():
                if title in options:
                    eval('self.designFor%s()' % title)
            else:
                self.L.set('No Module was selected.\nYou can exit and start again for\nother modules')
                self.LL.place(x=55, y=60)
                self.ST.destroy()
                self.BB.place(x=80, y=210)
                self.master.update()


if __name__ == "__main__":
    root = Tk()
    app = CELPIPTest(root)
    root.mainloop()