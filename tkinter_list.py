from tkinter import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")

def checking():
    t=lb.curselection()
    selected_value = [lb.get(i) for i in t]
    lab.config(text=",".join(selected_value))
    print(t)
    print(selected_value)
    t_add=[str(i+1) for i in t]
    
    lab['text'] = ",".join(t_add)
    #lab['text'] =f"{t_add}"
    #lab['text'] =f"{t_add} 번"

lb = Listbox(win)
lb.config(selectmode="extended")
lb.insert(0, "1번")
lb.insert(1, "2번")
lb.insert(2, "3번")
lb.insert(3, "4번")
lb.pack()

btn = Button(win)
btn.config(text= "옵션선택")
btn.config(command= checking)
btn.pack()

lab = Label(win)
lab.pack()

win.mainloop()