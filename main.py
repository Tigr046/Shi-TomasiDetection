import os
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
import uuid

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#FFFAFA')

initImagePath = ''
imageWithCornersDetection = None
def saveFile():
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(
                    ("png", "*.png"),  ("all files", "*.*")))
    if path is None:
        return
    cv2.imwrite(path, imageWithCornersDetection)

def detecionCorners():
    img = cv2.imread(initImagePath)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray_img, 10000, 0.7, 0)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()

        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
    tempFileName = str(uuid.uuid1()) + '.png'
    cv2.imwrite(tempFileName, img)
    imageWithCorners = PhotoImage(file=tempFileName)
    global imageWithCornersDetection
    imageWithCornersDetection = img
    imageText = Label(ws, text='Изображение с выделенными углами')
    image_label = Label(ws, image=imageWithCorners)
    imageText.grid(column=2, row=1)
    image_label.grid(column=2, row=2)
    cornersCount = Label(ws, text='Количество углов '+str(len(corners)))
    cornersCount.grid(column=2, row=3)
    saveButton = Button(ws, text='Сохрнаить изображение', command=saveFile)
    saveButton.grid(column=2, row=4)
    ws.mainloop()
    os.remove(tempFileName)


def selectfileclick():
    global initImagePath
    initImagePath = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if initImagePath == None:
        return
    imgWithOutCorners = PhotoImage(file=initImagePath)

    imageWithOutCornersText = Label(ws, text='Изначальное изображение')
    imageWithOutCorners_label = Label(ws, image=imgWithOutCorners)
    imageWithOutCornersText.grid(column=0, row=1)
    imageWithOutCorners_label.grid(column=0, row=2)
    detectionButton = Button(ws, text='Подсчитать углы', command=detecionCorners)
    detectionButton.grid(column=1, row=2)
    ws.mainloop()


selectFileBtn = Button(ws, text="Выбрать изображение", command=selectfileclick)
selectFileBtn.grid(column=0, row=0)
ws.mainloop()
