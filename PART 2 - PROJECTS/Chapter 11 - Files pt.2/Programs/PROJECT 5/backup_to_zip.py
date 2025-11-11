# Copies an entire folder and its contents into a ZIP file whose filename increments

import zipfile
import os
from pathlib import Path

def backup_to_zip(folder): 
    folder = Path(folder) # make sure folder is a Path obj
    
    nr = 1 # zip id nr
    while True: # this loop checks for if zip with current nr doesn't yet exist to avoid duplicate
        zip_filename = Path(folder.parts[-1] + '_' + str(nr) + '.zip')
        if not zip_filename.exists():
            break
        nr += 1 # increment nr if detects already existing file with that nr
        
    # create ZIP
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(Path.cwd() / zip_filename, 'w') # create ZIP in CWD! (slight change to original code)
    
    # Walk entire folder tree and compress files inside
    for folder_name, subfolder, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        print(f'Adding files in folder {folder_name} ...')
        
        for filename in filenames:
            print(f'Adding file {filename} ...')
            backup_zip.write(folder_name / filename)
        backup_zip.close()
    print('Done.')
        
backup_to_zip(Path.home() / 'spam')