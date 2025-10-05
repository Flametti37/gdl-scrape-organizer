'''
Used for files that follow a "postID_name_numberInSet.extension" format
i.e 12345_meow_2.jpg
'''
import os
from pathlib import Path
import shutil
import time

start = time.perf_counter()
rootInput = input('Enter the desired path:')

root = Path(rootInput).expanduser().resolve()

# main function
def patoOrganizer(path):

    prevFolder = None
    moved = 0
    failed = 0
    skipped = 0
    
    # Scans the selected dir, splits the DirEntry into parts
    try:
        with os.scandir(path) as listo:
            for i in listo:
                if i.is_file():
                    noExt = os.path.splitext(i.name)[0]
                    nameParts = noExt.split('_')
                    
                    # Reorganizes parts to allow for alphabetical sorting (ID_name -> name_ID)
                    if len(nameParts) >= 2:
                        numberSeg = nameParts[0]
                        nameSeg = nameParts[1].rstrip()
                        folderName = os.path.join(path, '_'.join([nameSeg, numberSeg]))
                        
                        # Creates new folder with the friendlier name
                        if folderName != prevFolder:
                            print(f"Working on {folderName}")
                            prevFolder = folderName
                            os.makedirs(folderName, exist_ok=True)                            
                       
                        # Moves current DirEntry into the newly created folder
                        try:    
                            shutil.move(i.path, folderName)
                            moved += 1
                        except Exception as e:
                            print(f"Error: {e}")
                            failed += 1
                    else:
                        skipped += 1
                        print(f"{i.name} Skipped: Does not match 'number_name' pattern.")
    
    except OSError as e:
        print('OSError:', e)

    # time tracking
    end = time.perf_counter()
    elapsed = (end - start)
    timeH = elapsed / 3600
    timeM = elapsed / 60
    timeS = elapsed % 60
    
    
    print(f"Operation Complete. {moved} files moved, {skipped} files skipped, {failed} files failed.")
    print(f"Ran for {timeH:2.0f} hours, {timeM:2.0f} minutes, {timeS:2.2f} seconds.")
    
patoOrganizer(root)
