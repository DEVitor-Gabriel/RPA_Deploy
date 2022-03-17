from tkinter import messagebox
import pandas as pd
from tkinter.messagebox import showinfo
import os

def base():
    try:
        user = os.getlogin()
        df = pd.read_excel(f'C:/Users/{user}/OneDrive - Conveste Serviços Financeiros/UiPath\Recebimento Automático/Horário e Robô por Operação.XLSX')

        operacoes = df['Operação']
        lista_operacoes = []

        for operacao in operacoes:  
            lista_operacoes.append(str(operacao))

        return lista_operacoes
    except:
        messagebox.showerror(title='Erro', message="""
        Erro na importação da base dados!
        Contate o administrador do sistema!
        """
        )
        exit()