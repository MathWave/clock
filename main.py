from tkinter import *
from time import asctime
from math import sin, cos, pi

########################################################################################################################

root = Tk()
root.title("Clock by MathWave")
root.geometry('250x350')
root.resizable(width=False, height=False)

########################################################################################################################

label_hours = Label(root, text='Часы:')
label_hours.place(x=10, y=13)

label_minutes = Label(root, text='Минуты: ')
label_minutes.place(x=10, y=43)

entry_hours = Entry(root)
entry_hours.place(x=70, y=10)

entry_minutes = Entry(root)
entry_minutes.place(x=70, y=40)

btn_set = Button(root, text='Установить!')
btn_set.place(x=5, y=70)
btn_set.bind("<Button-1>", lambda event: SetTime(int(entry_hours.get()), int(entry_minutes.get())))

btn_current = Button(root, text='Текущее время')
btn_current.place(x=115, y=70)
btn_current.bind("<Button-1>", lambda event: SetCurrentTime())

########################################################################################################################

canvas = Canvas(root, width=200, height=200, bg='white')
canvas.place(x=125, y=225, anchor='center')

def CreateClock():
    canvas.create_oval(5, 5, 195, 195, fill='black')
    canvas.create_oval(95, 95, 105, 105, fill='white')
    canvas.create_text(145, 28, text='1', fill='white')
    canvas.create_text(172, 55, text='2', fill='white')
    canvas.create_text(185, 100, text='3', fill='white')
    canvas.create_text(172, 145, text='4', fill='white')
    canvas.create_text(145, 172, text='5', fill='white')
    canvas.create_text(100, 185, text='6', fill='white')
    canvas.create_text(55, 172, text='7', fill='white')
    canvas.create_text(28, 145, text='8', fill='white')
    canvas.create_text(15, 100, text='9', fill='white')
    canvas.create_text(28, 55, text='10', fill='white')
    canvas.create_text(55, 28, text='11', fill='white')
    canvas.create_text(100, 15, text='12', fill='white')

CreateClock()

########################################################################################################################

def SetTime(hours, minutes):
    hours = hours % 12 + minutes / 60
    hours_x = 100 + cos(hours * pi / 6 - pi / 2) * 45
    hours_y = 100 + sin(hours * pi / 6 - pi / 2) * 45
    minutes_x = 100 + cos(minutes * pi / 30 - pi / 2) * 65
    minutes_y = 100 + sin(minutes * pi / 30 - pi / 2) * 65
    canvas.delete('all')
    CreateClock()
    canvas.create_line(100, 100, hours_x, hours_y, fill='white', width=3)
    canvas.create_line(100, 100, minutes_x, minutes_y, fill='white', width=1)


def SetCurrentTime():
    t = asctime().split()[3].split(':')
    SetTime(int(t[0]), int(t[1]))

########################################################################################################################

root.mainloop()
