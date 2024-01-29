import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font
import cv2

win = tk.Tk()
win.geometry("300x300")
win.title("kairos ai robotics")

win.resizable(False, False)
font = tk.font.Font(size = 20)
font1 = tk.font.Font(size = 10)
label = tk.Label(win, text = "kairos ai 로보틱스", font=font)
label1 = tk.Label(win, text = "청년아카데미", font=font1)
label.pack() # 위에서 부터 가운대로 출력 
label1.pack()

button = tk.Button(win, text="랜덤배경")
button.pack(pady=20) # 간격 뛰우기
win.mainloop()
