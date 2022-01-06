from tkinter import *
from tkinter import messagebox
from pyautogui import *
import time, threading, win32api

def status():
    messages.place(x = 340, y = 160)
    xp.place(x = 340, y = 240)
    time_elapsed.place(x = 340, y = 80)
    mins = 0
    secs = 0
    x = 0
    hoe = 0
    t = 0 
    index = 0
    for i in range(100000000):
        if x%int(seconds) == 0:
            index+=1 
        if index == len(commands):
          index = 0
        else: 
            pass
        
        if x%900 == 0 and (horse == 1 or horse == ""):
            hoe = True
        if x%int(seconds) == 0:
            click(pos)
            message = commands[int(index)]
            typewrite(message)
            t+=1
            typewrite(["enter"])
            if hoe:
                typewrite("pls buy hoe")
                typewrite(['enter'])
                time.sleep(4)
                typewrite("pls use hoe")
                typewrite(['enter'])
                hoe = False
            x += 1

            timer = '{:02d}:{:02d}'.format(mins, secs)
            time_elapsed.configure(text = timer)
            xp.configure(text = mins*20)
            messages.configure(text = t)
            time.sleep(1)
            secs += 1
            if secs%60 == 0:
                mins += 1
                secs = 0
        else:
            timer = '{:02d}:{:02d}'.format(mins, secs)
            time_elapsed.configure(text = timer)
            xp.configure(text = mins*20)
            messages.configure(text = t)
            time.sleep(1)
            secs += 1
            x += 1
            if secs%60 == 0:
                mins += 1
                secs= 0

def coordinates():
    global pos
    check = win32api.GetKeyState(0x02)
    while True:
        pos = position()
        pos = pos[:5]
        print(pos)
        Position.configure(text = pos)
        if win32api.GetKeyState(0x02) != check:
            quit()
    
def settings():
    global horse, commands, seconds
    horse = horseshoe.get()
    commands = commands_input.get(1.0, END).splitlines()
    if commands == [""]:
        messagebox.showinfo("This can't be done", "Mention the command you want to type!")
        return
    try:
        seconds = int(seconds_input.get())
    except:
        messagebox.showinfo("This can't be done", "Time must always be an integer!")
        return
    window.geometry('535x350')
    background.configure(image = calibrate)
    seconds_input.destroy()
    HOE.destroy()
    commands_input.destroy()
    Next.destroy()
    mouse_pos = threading.Thread(target=coordinates)
    mouse_pos.start()
    Calibrate.place(x =  180, y = 80)
    Position.place(x = 240, y = 310)

def stats():
    background.configure(image = stat)
    Calibrate.destroy()
    Position.destroy()
    statu = threading.Thread(target=status)
    statu.start()


window = Tk()
window.title("Discord Commander")
window.configure(background = "black")
window.geometry('840x600')
window.resizable(width = False, height = False)
back = PhotoImage(file = "GUI/set.png")
calibrate = PhotoImage(file = "GUI/calibrate.png")
next_button = PhotoImage(file = "GUI/button_next.png")
button_calibrate = PhotoImage(file = "GUI/button_calibrate.png")
stat =  PhotoImage(file = "GUI/stats.png")
background = Label(image = back)
background.place(x=-8,y=0)


commands_input = Text(window, height = 4, width = 76, bg = "#131313", bd = 0, fg = "white", font = ('Cascadia Mono', '10'))
commands_input.place(x = 120, y = 195)
commands_input.insert(1.0, "pls dig\npls fish\npls hunt\npls beg")

horseshoe = StringVar()
HOE = Checkbutton(window, variable = horseshoe, bg = "#131313", bd= 0, fg = "white",selectcolor = "black", onvalue = "on", offvalue = "off")
HOE.place(x = 356, y = 387)

seconds_input = Entry(window, width = 3, bg = "#131313", fg = "white", bd = 0, font= ("Aqua Grotesque", "14"))
seconds_input.place(x = 353, y= 477)
seconds_input.insert(0, "16")

Next = Button(window, image = next_button, bd = 0, bg = "#393939", activebackground = "#393939", cursor = "hand2", command = lambda:settings())
Next.place(x = 669, y = 9)

Calibrate = Button(window, image = button_calibrate, bd = 0, bg = "#000000", fg = "#000000", activebackground = "#000000", cursor = "hand2", command = lambda:stats())
Calibrate.place(x =  100000, y = 80)

Position = Label(window, text = "nothing", bg = "#393939", fg = "white")

messages = Label(window, text = "nothing", bg = "#131313", fg = "white", font= ("Aqua Grotesque", "13"))

xp = Label(window, text = "nothing", bg = "#131313", fg = "white", font= ("Aqua Grotesque", "13"))

time_elapsed = Label(window, text = "nothing", bg = "#131313", fg = "white", font= ("Aqua Grotesque", "13"))

window.mainloop()