from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Система массовых Репортов На Скретчера")
window.geometry('900x300')
lbl = Label(window, text="ПРИВЕТ! Это бот Спаммер. Он спамит жалобы в скретч тим!", font=("Arial Bold", 17))
lbl2 = Label(window,
             text="Сначала нужно предоставить данные аккаунта с которого будете спамить репортами, а также цель и тип жалобы",
             font=("Arial Bold", 14))
lbl3 = Label(window, text="Username в Scratch", font=("Arial Bold", 10))
lbl4 = Label(window, text="Password в скретче", font=("Arial Bold", 10))
lbl5 = Label(window, text="Цель в скретче(username)", font=("Arial Bold", 10))
lbl6 = Label(window, text="Тип Жалобы", font=("Arial Bold", 10))

user = Entry(window, width=20)
password = Entry(window, width=20)
pap = Entry(window, width=20)


def Run():
    from scratchclient import ScratchSession
    s = ScratchSession(user.get(), password.get())
    c = s.get_user(pap.get())
    x = combo.get()
    while True:
        try:
            c.report(x)
        except:
            pass


but = Button(window, command=Run, text="Начать Атаку")
combo = Combobox(window)
combo["values"] = ("Имя пользователя",
                   "Icon",
                   "About Me",
                   "What I'm Working On")
lbl.pack()
lbl2.pack()
lbl3.pack()
user.pack()
lbl4.pack()
password.pack()
lbl5.pack()
pap.pack()
lbl6.pack()
combo.pack()
but.pack()

window.mainloop()
