from tkinter import *

win = Tk()
win.geometry("700x500")
win.option_add("*Font", "맑은고딕 20")
win.title("grid place")


btn_list = []
col_num = 4
row_num = 3

for i in range(0, row_num):
    for j in range(0, col_num):
        btn = Button(win)
        btn.config(text=f"{i},{j}")
        btn.grid(column=j, row = i ,padx=2, pady=2)
        btn_list.append(btn)


btn_long = Button(win)
btn_long.config(text="(2,0)")
btn_long.grid(column=3, row=0 , rowspan=2)
btn_long.config(width=5, height=3)

btn_wide =Button(win)
btn_wide.config(text="(1,2)")
btn_wide.grid(column=1, row=2, rowspan=2)
btn_wide.config(width=10, height=1)

btn_one = Button()
win.mainloop()


