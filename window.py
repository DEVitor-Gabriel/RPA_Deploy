from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1184x678")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 678,
    width = 1184,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    563.0, 352.5,
    image=background_img)

canvas.create_text(
    210.0, 160.5,
    text = "Recebimento Automático",
    fill = "#ffffff",
    font = ("DoppioOne-Regular", int(26.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    218.0, 301.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 33.5, y = 281,
    width = 369.0,
    height = 39)

canvas.create_text(
    197.5, 245.5,
    text = "Selecione a operação:",
    fill = "#000000",
    font = ("DoppioOne-Regular", int(19.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    218.0, 410.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 33.5, y = 390,
    width = 369.0,
    height = 39)

canvas.create_text(
    196.5, 354.5,
    text = "Selecione o BOT:",
    fill = "#000000",
    font = ("DoppioOne-Regular", int(19.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 35, y = 479,
    width = 372,
    height = 85)

window.resizable(False, False)
window.mainloop()
