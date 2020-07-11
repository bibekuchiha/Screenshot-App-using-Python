import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = '/root/Documents/python projects/screenshots/{}.png'.format(name)#change your path to save your screenshot
    img = pyautogui.screenshot(name)
    img.show()

screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

buttom = tk.Button(
    frame,
    text = 'Take Screenshot',
    command = screenshot
)
buttom.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text = 'Quit',
    command = quit)
close.pack(side=tk.LEFT)

root.mainloop()