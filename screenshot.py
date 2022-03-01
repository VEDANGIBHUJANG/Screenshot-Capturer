#project 1
#pip install pyautogui
import time
import pyautogui
import tkinter as tk

#pip install pyautogui,pip install pillow
def screenshot():
    name =int(round(time.time()*1000)) #generate random no. for image
    name='D:/Python projects/screenshots data/{}.png'.format(name)
    #time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
     frame,
     text="Take Screenshot",
     command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
     frame,
     text="QUIT",
     command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
   