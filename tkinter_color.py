import tkinter as tk
import serial

class ArduinoGUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Ultrasonic Visualization")

        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        self.serial_port = serial.Serial('COM5', 9600, timeout=1)
        self.master.after(100, self.update_distance)

    def update_distance(self):
        
        distance_str = self.serial_port.readline().decode().strip()

        try:
            distance = int(distance_str)
        except ValueError:
            distance = 0

        self.update_color(distance)

        self.master.after(100, self.update_distance)

    def update_color(self, distance):
       
        if distance < 10:
            color = "red"
        elif distance < 15:
            color = "orange"
        elif distance < 20:
            color = "white"
        elif distance < 25:
            color = "green"
        elif distance < 30:
            color = "blue"
        elif distance >= 31:
            color = "purple"
        else:
            color = "white"

        self.canvas.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoGUI(root)
    root.mainloop() 