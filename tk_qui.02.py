import tkinter as tk
import tkinter.font
import random
win = tk.Tk()
win.geometry("300x300")
win.title("kairos ai robotics")

def selection_center():
    centers =["가산","강남", "종로"]
    selection_center = random.choice(centers)
    label1["text"] = f"선택된 센터: {selection_center}"
    

def reset():
    label1["text"] = "청년아카데미"

win.resizable(False, False)
font = tk.font.Font(size = 20)
font1 = tk.font.Font(size = 10)
label = tk.Label(win, text = "kairos ai 로보틱스", font=font)
label1 = tk.Label(win, text = "청년아카데미", font=font1)
label.pack() # 위에서 부터 가운대로 출력 
#label1.pack() # 순서대로 가운데 출력
label1.place(relx = 0.5 , rely= 0.5 , anchor="center") #원하는 좌표값으로 위치값 이동 anchor = 정렬 옵션, rlex = x좌표 이동 , rely = y좌표이동( 0 ~ 1값 사이) 


button = tk.Button(win, text="센터 선택", command=selection_center, bg = "yellow") #command 
button.pack(pady=20) # 간격 뛰우기
button1 = tk.Button(win, text="초기화", command=reset, bg = "lightpink")
button1.pack(pady=20) # 간격 뛰우기

win.mainloop()
