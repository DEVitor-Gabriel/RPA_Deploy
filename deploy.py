import os
from pathlib import Path
import shutil


def deploy():
    orig = Path('//cvt-d589/c$/Users/UIPATH/Documents/UiPath')
    dest1 = Path('//cvt-d293/c$/QAStransfer/UiPath')
    dest2 = Path('//cvt-d293/c$/QAStransfer2/UiPath')
    dests = [dest1, dest2]

    for dest in dests:
        if os.path.exists(dest):
            shutil.rmtree(dest)
            
        shutil.copytree(orig, dest)
