import os
from pathlib import Path
import shutil
from tkinter import messagebox
from datetime import datetime




def deploy():

    try:
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d-%m-%Y %H-%M')

        cvt_qas = 'cvt-d589'
        cvt_prod1 = 'cvt-d277'
        cvt_prod2 = 'cvt-d32'

        orig_pkg = Path(f'//{cvt_qas}/C/ProgramData/UiPath/Packages')
        dest1_pkg = Path(f'//{cvt_prod1}/C/ProgramData/UiPath/Packages')
        dest2_pkg = Path(f'//{cvt_prod2}/C/ProgramData/UiPath/Packages')
        dests_pkg = [dest1_pkg, dest2_pkg]


        orig = Path(f'//{cvt_qas}/C/Users/UIPATH/Documents/UiPath')
        dest1 = Path(f'//{cvt_prod1}/C/Users/UIPATH/Documents/UiPath')
        dest2 = Path(f'//{cvt_prod2}/C/Users/UIPATH/Documents/UiPath')
        dests = [dest1, dest2]


        for dest in dests:
            if os.path.exists(dest):
                # shutil.rmtree(dest)
                str_dest = str(dest)
                split_uipath =  str_dest.split('UiPath')
                dest_backup = Path(f'{split_uipath[0]}Backup/{data_e_hora_em_texto}')

                shutil.move(dest, dest_backup)
            
            shutil.copytree(orig, dest)

        for dest in dests_pkg:
            if os.path.exists(dest):
                # shutil.rmtree(dest)
                str_dest = str(dest)
                split_uipath =  str_dest.split('Packages')
                dest_backup = Path(f'{split_uipath[0]}Backup/{data_e_hora_em_texto}')

                shutil.move(dest, dest_backup)
            
            shutil.copytree(orig_pkg, dest)

    except:
        messagebox.showerror(title='Erro', message="""
        Erro no deploy!
        Contate o administrador do sistema!
        """
        )