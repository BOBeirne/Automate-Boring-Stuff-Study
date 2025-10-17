# Copies an entire folder and its contents into a ZIP file whose filename increments

import zipfile
import os
from pathlib import Path

def backup_to_zip(folder): 
    folder = Path(folder) # make sure folder is a Path obj
    
    nr = 1
    while True:
        
        zip_filename = Path(folder.parts[-1] + '_' + str(nr) + '.zip')
        if not zip_filename.exists():
            break
        nr += 1
    # TODO: create ZIP
    # TODO: walk entire folder and compress files inside
    print('Done.')
        
backup_to_zip(Path.home() / 'spam')