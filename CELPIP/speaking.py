import tkinter.ttk

import sounddevice as sd
import soundfile as sf
from tkinter import *
import json
import random
import time
from datetime import datetime
import os
from tkinter import PhotoImage
import speech_recognition as sr
import pyttsx3


def getJson():
    with open("questions.json") as fp:
        qus = json.load(fp)
    return qus


def prepCounter(preptime):
    preptime -= 1
    while preptime > -1:
        sec1.set(preptime)
        preptime -= 1
        master.update()
        time.sleep(1)


def durationCounter(duration):
    duration -= 1
    temp = 0
    while duration > -1:
        sec2.set(duration)
        duration -= 1
        temp += 1
        master.update()
        total = duration + temp + 1
        print("%", ((total - duration) / total) * 100, "total", total, "duration", duration)
        progBarUpdate(((total - duration) / total) * 100)
        time.sleep(1)


def durationCounterW(duration):
    temp = 0
    duration = duration * 60
    while duration > -0.5:
        sec2.set(int(duration / 60))
        duration -= 0.5
        temp += 0.5
        master.update()
        total = duration + temp
        print("%", ((total - duration) / total) * 100, "total", total, "mins", duration / 60)
        progBarUpdate(((total - duration) / total) * 100)
        WW.set('Word-count: %s' % len(TT.get('1.0', END).split(' ')))
        time.sleep(0.5)


def Voice_rec(duration, name):
    engine = pyttsx3.init()
    text = "Please start speaking now"
    engine.say(text)
    engine.runAndWait()

    fs = 48000
    r = sr.Recognizer()
    # seconds
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    durationCounter(duration)
    progBarStop()
    # sd.wait() removed as putting wait time
    Q.set("Please wait writing your audio file and audio to text file")
    master.update()
    # Save as FLAC file at correct sampling rate
    sf.write(name, myrecording, fs)
    try:
        with sr.AudioFile(os.path.join(os.getcwd(), name)) as audio:
            data = r.record(audio)
            text = r.recognize_google(data)
            filename = name.replace('flac', 'txt')
            with open(filename, 'w') as file:
                file.write(text)
    except:
        Q.set('Error in writing audio to text file')
        master.update()
        time.sleep(2)


def setImage(path):
    image = PhotoImage(file=path)
    can.create_image(5, 400, anchor=SW, image=image)
    can.image = image


def showRadiobutton():
    rad1.place(x=150, y=200)
    rad2.place(x=500, y=200)


def destroyRadiobutton():
    rad1.destroy()
    rad2.destroy()


def progBarUpdate(percVar):
    myProgBar['value'] = percVar
    master.update()


def progBarStop():
    myProgBar.stop()


def finish():
    master.destroy()


def designForSpeakingTask():
    master.title("Speaking-Task")
    master.geometry("900x600")
    ST.destroy()
    can.place(x=5, y=550)
    var.set(1)

    PT.place(x=650, y=30)
    PTE.place(x=850, y=30)
    sec1.set('00')

    RT.place(x=650, y=60)
    RTE.place(x=850, y=60)
    sec2.set('00')

    myProgBar.place(x=100, y=5)

    ff.set("Close Test")
    FT.place(x=700, y=550)

    timer.set("Record-time remaining: ")

    master.update()

    for ind in range(startfrom, 9):
        data = jData['SpeakingTask'][str(ind)]
        noOfQ = (len(data) - 3) if ind != 5 else (len(data) - 3) / 2

        T.set("Task:-%s : %s" % (ind, data['0']))
        master.update()

        randV = random.randrange(1, noOfQ + 1)
        duration = data['duration']
        preptime = data['preptime']

        qus = data[str(randV)]
        Q.set("Qus:- %s" % qus)
        master.update()

        if ind in (3, 4, 5, 8):
            currPath = os.path.join(os.getcwd(), "images/Task%s/%s.png" % (ind, randV))
            if ind == 5:
                setImage(currPath)
                showRadiobutton()
                prepCounter(60)
                currPath = os.path.join(os.getcwd(), "images/Task%s/%s_%s.png" % (ind, randV, var.get()))
                destroyRadiobutton()
                qus = data["%s_2" % randV]
                Q.set("Q:- %s" % qus)
            setImage(currPath)

        prepCounter(preptime)
        name = "%s/S/%s_%s.flac" % (testtime, ind, testhourmin)
        Voice_rec(duration, name)
        setImage(path)
        Q.set("Qus:- ")


def designForWritingTask():
    master.title("Writing-Task")
    master.geometry("900x900")
    master.resizable(False, False)
    ST.destroy()
    can.place(x=5, y=850)

    PT.place(x=650, y=30)
    PTE.place(x=850, y=30)
    sec1.set('00')

    RT.place(x=650, y=60)
    RTE.place(x=850, y=60)
    sec2.set('00')

    myProgBar.place(x=100, y=5)

    ff.set("Close Test")
    FT.place(x=700, y=860)

    timer.set("Writing-time remaining: ")

    WC.place(x=500, y=860)

    TT.place(x=60, y=220)

    master.update()

    for ind in range(1, 3):
        data = jData['WritingTask'][str(ind)]
        noOfQ = len(data) - 3

        T.set("Task:-%s : %s" % (ind, data['0']))
        master.update()

        randV = random.randrange(1, noOfQ + 1)

        duration = data['duration']

        qus = data[str(randV)]
        Q.set("Qus:- %s" % qus)
        master.update()

        durationCounterW(duration)
        text = TT.get('1.0', END)
        name = "%s/W/%s_%s.txt" % (testtime, ind, testhourmin)
        writeTexttoFile(name, text)
        TT.delete('1.0', END)
        master.update()
    TT.destroy()
    WC.destroy()


def writeTexttoFile(name, text):
    with open(name, 'w') as fp:
        fp.write(text)


def createFolders():
    try:
        print(os.path.join(wd, f'{testtime}'))
        os.makedirs(os.path.join(wd, f'{testtime}\W'), exist_ok=True)
        os.makedirs(os.path.join(wd, f'{testtime}\S'), exist_ok=True)
        os.makedirs(os.path.join(wd, f'{testtime}\R'), exist_ok=True)
        os.makedirs(os.path.join(wd, f'{testtime}\L'), exist_ok=True)
    except:
        print('error')
        pass


def on_click():
    createFolders()
    options = [var1.get(), var2.get(), var3.get(), var4.get()]
    print(options)
    c1.destroy()
    c2.destroy()
    c3.destroy()
    c4.destroy()

    for title in jData.keys():
        if title in options:
            eval('designFor%s()' % title)


if __name__ == "__main__":
    master = Tk()
    master.title("CELPIP Test")
    master.geometry("300x300")
    master.resizable(False, False)
    jData = getJson()
    sec1 = StringVar()
    sec2 = StringVar()

    Q = StringVar()
    WW = StringVar()
    T = StringVar()
    ss = StringVar()
    ff = StringVar()
    var = IntVar()
    timer = StringVar()

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    imagePath = StringVar()

    testtime = datetime.now().strftime("%d_%m")
    testhourmin = datetime.now().strftime('%H_%M')

    startfrom = 0

    TT = Text(master, height=35, width=85, font='Helvetica14')

    PT = Label(master, text="Prep-time remaining: ", font='Helvetica14', justify=LEFT)
    PTE = Entry(master, textvariable=sec1, width=2, font='Helvetica14')

    RT = Label(master, textvariable=timer, font='Helvetica14')
    RTE = Entry(master, textvariable=sec2, width=2, font='Helvetica14')

    Label(master, textvariable=Q, font='Helvetica14', justify=LEFT).place(x=50, y=90)
    Label(master, textvariable=T, font='Helvetica14', justify=LEFT).place(x=50, y=30)
    WC = Label(master, textvariable=WW, font='Helvetica14', justify=LEFT)
    WW.set('Word-count: 0')

    ST = Button(master, textvariable=ss, command=on_click, width=20)
    ss.set("Start Test")
    FT = Button(master, textvariable=ff, command=finish, width=20)
    ff.set("Exit Test")
    ST.place(x=80, y=150)
    FT.place(x=80, y=200)

    can = Canvas(master, width=300, height=50)
    can.place(x=1, y=240)
    wd = os.getcwd()
    path = os.path.join(wd, "images/developerBy.png")
    image = PhotoImage(file=path)
    can.create_image(1, 50, anchor=SW, image=image)

    myProgBar = tkinter.ttk.Progressbar(master, orient=HORIZONTAL, length=700, mode='determinate')

    rad1 = Radiobutton(master, text="Option 1", variable=var, value=1)
    rad2 = Radiobutton(master, text="Option 2", variable=var, value=2)

    c1 = Checkbutton(master, text='WritingTask', variable=var1, onvalue='WritingTask', offvalue='')
    c1.place(x=80, y=10)
    c2 = Checkbutton(master, text='SpeakingTask', variable=var2, onvalue='SpeakingTask', offvalue='')
    c2.place(x=80, y=40)
    c3 = Checkbutton(master, text='ReadingTask', variable=var3, onvalue='ReadingTask', offvalue='')
    c3.place(x=80, y=70)
    c4 = Checkbutton(master, text='ListeningTask', variable=var4, onvalue='ListeningTask', offvalue='')
    c4.place(x=80, y=100)

    mainloop()
