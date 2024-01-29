import tkinter as tk
import tkinter.font  # tkinter 문자 폰트 지정리이브러리
import cv2
from PIL import Image, ImageTk
import random
def selection_center(): # center 배열(list)로 저장하여 랜덤 설정
    centers =["가산","강남", "종로"]
    selection_center = random.choice(centers) #랜덤으로 list 에서 하나 선택
    label1["text"] = f"선택된 센터: {selection_center}" # 선택한 결과 출력
    path ={"가산" : r"C:\Users\user\Documents\KAIROS\image\kairos_01.png",
           "강남" : r"C:\Users\user\Documents\KAIROS\image\kairos02.png",
           "종로" : r"C:\Users\user\Documents\KAIROS\image\kairos_03.png"}

    image_path = path.get(selection_center, "") 
    if image_path:
        image = Image.open(image_path)
        image = image.resize((150, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image=photo

def reset():
    label1["text"] = "청년아카데미"
    image = Image.open(image_pate)
    image = image.resize((150, 150), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image=photo


win = tk.Tk() # tkinter 객체 생성 모든코드 아래에 입력 해야 동작
win.geometry("300x300") # window 창크기 설정 
win.title("kairos ai robotics") # window 명 설정
win.resizable(False, False) # GUI 상으로 사이즈 변경여부 설정
font = tk.font.Font(size = 20) # tkinter font 설정 부분 
font1 = tk.font.Font(size = 10)
label = tk.Label(win, text = "kairos ai 로보틱스", font=font) # window 내에 텍스트 출력
label1 = tk.Label(win, text = "청년아카데미", font=font1) 
label.pack() # 위에서 부터 가운대로 출력 
image_pate = r"C:\Users\user\Documents\KAIROS\image\image.png" 
image = Image.open(image_pate)
image = image.resize((150,100), Image.LANCZOS) # Image.LANCZOS 이미지 해상도 올려주는 기능
poto = ImageTk.PhotoImage(image)
image_label = tk.Label(win, image = poto)
image_label.image  = poto
image_label.pack()
label1.pack() # 순서대로 가운데 출력
#label1.place(relx = 0.5 , rely= 0.5 , anchor="center") #원하는 좌표값으로 위치값 이동 anchor = 정렬 옵션, rlex = x좌표 이동 , rely = y좌표이동( 0 ~ 1값 사이) 

#image_label.place(relx=0.5, rely=0.5, anchor="center")

button = tk.Button(win, text="센터 선택", command=selection_center, bg = "yellow") #command 
button.pack(pady=5) # 간격 뛰우기
button1 = tk.Button(win, text="초기화", command=reset, bg = "lightpink")
button1.pack(pady=5) # 간격 뛰우기

win.mainloop()
