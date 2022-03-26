from tkinter import messagebox
from openpyxl import workbook, load_workbook
import os

def atualizar_planilha(operacao, bot):

    try:
        user = os.getlogin()
        planilha = load_workbook(f'C:/Users/{user}/OneDrive - Conveste Serviços Financeiros/UiPath\Recebimento Automático/Horário e Robô por Operação.XLSX')

        sheet = planilha.active

        for celula in sheet['A']:
            if celula.value == operacao:
                linha = celula.row
                sheet[f'C{linha}'] = bot
        
        planilha.save(f'C:/Users/{user}/OneDrive - Conveste Serviços Financeiros/UiPath\Recebimento Automático/Horário e Robô por Operação.XLSX')

    except:
        messagebox.showerror(title='Erro', message="""
        Erro para atualizar a planilha online!
        Contate o administrador do sistema!
        """
        )