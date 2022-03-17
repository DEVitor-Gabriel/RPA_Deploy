from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo



def btn_clicked():
    if (entry0.get() == '' or entry1.get() == ''):
        print('erro')
        showinfo(title='Erro', message='Todos os campos precisam ser preenchidos')
    else:
        print(f"Operação Selecionada {entry0.get()}")
        print(f"Bot Selecionado {entry1.get()}")


window = Tk()
window.title('RPA Deploy')

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
    218.0, 299.5,
    image = entry0_img)


def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )
    entry0['str'] = 'disable'

selected_month = StringVar()

entry0 = ttk.Combobox(window, 
                            # bd = 0,
                            # bg = "#ffffff",
                            # highlightthickness = 0,
                            font=("DoppioOne-Regular", int(16.0)),
                            
                            textvariable=selected_month)

entry0['values'] = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']

# entry0.bind('<<ComboboxSelected>>', month_changed)
# entry0.current(0)
entry0['state'] = 'readonly'




entry0.place(
    x = 33.5, y = 281,
    width = 369.0,
    height = 39)

canvas.create_text(
    197.5, 260.5,
    text = "Selecione a operação:",
    fill = "#000000",
    font = ("DoppioOne-Regular", int(19.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    218.0, 408.5,
    image = entry1_img)

entry1 = ttk.Combobox(window, 
                            # bd = 0,
                            # bg = "#ffffff",
                            # highlightthickness = 0,
                            font=("DoppioOne-Regular", int(16.0)),
                            values=[
                                    "01", 
                                    "03"])

entry1.set('03')

entry1.place(
    x = 33.5, y = 390,
    width = 369.0,
    height = 39)

canvas.create_text(
    196.5, 370.5,
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
