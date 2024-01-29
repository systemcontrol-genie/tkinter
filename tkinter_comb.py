from tkinter import *
from tkinter.ttk import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("comb box")

def clicking():
    label['text'] = cbox.get() # text 소문자 입력 할것 Text로 입력시 오류 발생.
    #print(cbox.get()) cbox 값 불러오기

cbox_list = ["1", "2", "3"]
cbox = Combobox(win)
cbox.config(values= cbox_list)
cbox.pack()

btn = Button(win)
btn.config(text ="선택")
btn.config(command=clicking)
btn.pack()

label =Label(win)
label.pack()
win.mainloop()
