from openpyxl import workbook, load_workbook
import os

def atualizar_planilha(operacao, bot):
    user = os.getlogin()
    planilha = load_workbook(f'C:/Users/{user}/OneDrive - Conveste Serviços Financeiros/UiPath\Recebimento Automático/Horário e Robô por Operação.XLSX')

    sheet = planilha.active

    for celula in sheet['A']:
        if celula.value == operacao:
            linha = celula.row
            sheet[f'C{linha}'] = int(bot)
    
    planilha.save(f'C:/Users/{user}/OneDrive - Conveste Serviços Financeiros/UiPath\Recebimento Automático/Horário e Robô por Operação.XLSX')
