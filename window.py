from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from pandas import options
from base import base
from atualizar_planilha import atualizar_planilha
from deploy import deploy

lista_operacoes = base()

def btn_clicked():
    b0['state'] = DISABLED,
    OperacaoComboBox['state'] = 'disabled'
    BotComboBox['state'] = 'disabled'

    if (OperacaoComboBox.get() == '' or BotComboBox.get() == ''):
        messagebox.showerror(title='Erro', message='Todos os campos precisam ser preenchidos')
    else:
        msg_box = messagebox.askyesno(title='Confirmar', message='Tem certeza que deseja realizar o Deploy ?')

        if (msg_box == True):
            deploy()
            atualizar_planilha(OperacaoComboBox.get(),BotComboBox.get())
            messagebox.showinfo(title='Finalizado', message='Deploy finalizado com sucesso!')


    OperacaoComboBox['state'] = 'readonly'
    BotComboBox['state'] = 'readonly'
    b0['state'] = ACTIVE,



window = Tk()
window.title('RPA Deploy')
window.iconphoto(False, PhotoImage(file='./icon/icon.png'))

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

background_img = PhotoImage(file = f"images/background.png")
background = canvas.create_image(
    563.0, 352.5,
    image=background_img)

canvas.create_text(
    210.0, 160.5,
    text = "Recebimento Automático",
    fill = "#ffffff",
    font = ("DoppioOne-Regular", int(26.0)))

OperacaoComboBox_img = PhotoImage(file = f"images/img_textBox0.png")
OperacaoComboBox_bg = canvas.create_image(
    218.0, 299.5,
    # image = OperacaoComboBox_img
    )

OperacaoComboBox = ttk.Combobox(window, 
                            font=("DoppioOne-Regular", int(16.0)),
                            )

OperacaoComboBox['values'] = lista_operacoes

# OperacaoComboBox.bind('<<ComboboxSelected>>', month_changed)
# OperacaoComboBox.current(0)
OperacaoComboBox['state'] = 'readonly'

OperacaoComboBox.place(
    x = 33.5, y = 281,
    width = 369.0,
    height = 39)

canvas.create_text(
    197.5, 260.5,
    text = "Selecione a operação:",
    fill = "#000000",
    font = ("DoppioOne-Regular", int(19.0)))

BotComboBox_img = PhotoImage(file = f"images/img_textBox1.png")
BotComboBox_bg = canvas.create_image(
    218.0, 408.5,
    # image = BotComboBox_img
    )

BotComboBox = ttk.Combobox(window, 
                            font=("DoppioOne-Regular", int(16.0)),                      
                            values=[
                                    1, 
                                    3])

BotComboBox.set(3)
BotComboBox['state'] = 'readonly'

BotComboBox.place(
    x = 33.5, y = 390,
    width = 369.0,
    height = 39)

canvas.create_text(
    196.5, 370.5,
    text = "Selecione o BOT:",
    fill = "#000000",
    font = ("DoppioOne-Regular", int(19.0)))

img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(
    background= '#ffffff',
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
