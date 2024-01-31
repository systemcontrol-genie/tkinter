from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import serial
import cv2
delay = 33
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
#port = "COM5"
#ser = serial.Serial(port, 9600, timeout = 1)
#def send_command(command):
#    ser.write(command.enable())

#def send_angle():
#    s = ent.get()
#    ser.write(s.encode())

#   send_command()
   
#def send_angle1():
#    s = ent1.get()
#    ser.write(s.encode())

#def send_angle2():
#    s = ent2.get().split(',')
#    ser.write(s.encode())



def update_label(label, slider):
    label.config(text=str(round(slider.get(), 1)))

def save():
    if (ent.winfo_exists() and rv.get() ==0):
        ent.delete(0,END)
    if (ent1.winfo_exists() and rv.get() ==1):
        ent1.delete(0, END)
    if (ent2.winfo_exists() and rv.get() ==2):
        ent2.delete(0, END)

    if (rv.get() == 0):
        ent.insert(END, round(slider.get()))
        ent.insert(END, str(","))
        ent.insert(END, round(slider1.get()))
        ent.insert(END, str(","))
        ent.insert(END, round(slider2.get()))
        ent.insert(END, str(","))
        ent.insert(END, round(slider3.get()))
    if (rv.get() == 1):
        ent1.insert(END, round(slider.get()))
        ent1.insert(END, str(","))
        ent1.insert(END, round(slider1.get()))
        ent1.insert(END, str(","))
        ent1.insert(END, round(slider2.get()))
        ent1.insert(END, str(","))
        ent1.insert(END, round(slider3.get()))

    if (rv.get() == 2):
        ent2.insert(END, round(slider.get()))
        ent2.insert(END, str(","))
        ent2.insert(END, round(slider1.get()))
        ent2.insert(END, str(","))
        ent2.insert(END, round(slider2.get()))
        ent2.insert(END, str(","))
        ent2.insert(END, round(slider3.get()))


# 서보모터 4개 , 관절 4개 조절, 구동 버튼 누를시 구동 되어야함.a, b, c 지점 이동, 각도 등록
win = Tk()
#win.geometry("700x500")
win.title("test")
lbl1 = Label(win)
lbl1.grid(row=0, column=4, rowspan= 8)
win.option_add("*Font", "맑은고딕 20")
lab = Label(win, text="#1")
slider = Scale(win, from_=0, to=180, orient=HORIZONTAL)
lab1 = Label(win, text="#2")
slider1 = Scale(win, from_=0, to=180, orient=HORIZONTAL)
lab2 = Label(win, text="#3")
slider2 = Scale(win, from_=0, to=180, orient=HORIZONTAL)
lab3 = Label(win, text="#4")
slider3 = Scale(win, from_=0, to=180, orient=HORIZONTAL)
lab4 = Label(win)
lab4 = Label(win, text="")
lab4.config(text=f"{slider.get()}")
lab5 = Label(win)
lab5 = Label(win, text="")
lab5.config(text=f"{slider1.get()}")
lab6 = Label(win)
lab6 = Label(win, text="")
lab6.config(text=f"{slider2.get()}")
lab7 = Label(win)
lab7 = Label(win, text="")
lab7.config(text=f"{slider3.get()}")
lab8 = Label(win, text="번호")
lab9 = Label(win, text="각도 등록 확인")
lab.grid(row=0, column=0)
slider.grid(row=0, column=2)
btn = Button(win)
btn.config(text="저장", command=save)
btn.grid(row=0, column=3)
lab1.grid(row=1, column=0)
slider1.grid(row=1, column=2)
lab2.grid(row=2, column=0)
slider2.grid(row=2, column=2)
lab3.grid(row=3, column=0)
slider3.grid(row=3, column=2)
lab4.grid(row=0, column=1)
lab5.grid(row=1, column=1)
lab6.grid(row=2, column=1)
lab7.grid(row=3, column=1)
lab8.grid(row=4, column=0)
lab9.grid(row=4, column=1)
slider.config(command=lambda value, label=lab4, s=slider: update_label(label, s) )
slider1.config(command=lambda value, label=lab5, s=slider1: update_label(label, s) )
slider2.config(command=lambda value, label=lab6, s=slider2: update_label(label, s) )
slider3.config(command=lambda value, label=lab7, s=slider3: update_label(label, s) )
rv = IntVar()
rb1 = Radiobutton(win, text="position1", value=0, variable=rv)
rb2 = Radiobutton(win, text="position2", value=1, variable=rv)
rb3 = Radiobutton(win, text="position3", value=2, variable=rv)
rb1.grid(row=5, column=0)
rb2.grid(row=6, column=0)
rb3.grid(row=7, column=0)
ent = Entry(win)
ent.grid(row=5, column=1)
ent1 = Entry(win)
ent1.grid(row=6, column=1) 
ent2 = Entry(win)
ent2.grid(row=7, column=1)
label = Label(win)
label.grid()
btn1 = Button(win)
btn1.config(text="동작")
btn1.grid(row=5, column=2)
btn2 = Button(win)
btn2.config(text="동작")
btn2.grid(row=6, column=2)
btn3 = Button(win)
btn3.config(text="동작")
btn3.grid(row=7, column=2)
def video_play():
    ret, frame = cap.read() # 프레임이 올바르게 읽히면 ret은 True
    if not ret:
        cap.release() # 작업 완료 후 해제
        return
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(frame) # Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=img) # ImageTk 객체로 변환
    # OpenCV 동영상
    lbl1.imgtk = imgtk
    lbl1.configure(image=imgtk)
    lbl1.after(10, video_play)
video_play()

win.mainloop()