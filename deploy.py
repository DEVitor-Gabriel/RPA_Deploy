import os
from pathlib import Path
import shutil


def deploy():
    orig = Path('//cvt-d589/c$/Users/UIPATH/Documents/UiPath')
    dest = Path('//cvt-d293/c$/QAStransfer/UiPath')
    print(orig)
    print(dest)

    if os.path.exists(dest):
        shutil.rmtree(dest)
        
    shutil.copytree(orig, dest)