import os
from pathlib import Path
import shutil

rootInput = input('Enter the desired path:')
singleItem = None

root = Path(rootInput).expanduser().resolve()

# Single photos, Reels, and Highlights are have 19char filenames. This is to select what will be dealt with.

while True:
    print("Please Select a Post Type:\n1: Reels + Single Images\n2: Highlights\n3: None")
    choice = input('Enter Choice:')
    
    match choice:
        case '1':
            singleItem = '_Reels'
            singlePhoto = '_SinglePhoto'
            break;
        case '2':
            singleItem = '_Highlights'
            singlePhoto = '_Highlights'
            break;
        case '3':
            singleItem = '.'
            singlePhoto = '.'
            break;
        case _:
            print('Please enter a valid selection.')

# main function
def instaOrganizer(path, singleItem, singlePhoto):

    prevFolder = None
    moved = 0
    failed = 0
    SCount = 0
    
    try:
        with os.scandir(path) as listo:
            for i in listo:
                if i.is_file():
                    noExt = os.path.splitext(i.name)[0]
                    ext = os.path.splitext(i.name)[1]
                    
                    
                    if '_' not in noExt:
                        if ext in ['.mp4', '.mov', '.webm', '.m4a', '.ts', '.avi']:
                            singles = os.path.join(path,singleItem)
                        else:
                            singles = os.path.join(path,singlePhoto)
                            
                        os.makedirs(singles, exist_ok=True)
                        shutil.move(i.path, singles)
                        SCount += 1
                    else:
                        nameParts = noExt.split('_')
                        numberSeg = nameParts[0]
                        folderName = os.path.join(path, numberSeg[:6])

                        if folderName != prevFolder:
                            print(f"Working on {folderName}")
                            prevFolder = folderName
                            os.makedirs(folderName, exist_ok=True)                        
                        try:    
                            shutil.move(i.path, folderName)
                            moved += 1
                        except Exception as e:
                            print(f"Error: {e}")
                            failed += 1
    except OSError as e:
        print('OSError:', e)
    
    print(f"Operation Complete. {moved} files moved, {SCount} Singles moved, {failed} files failed.")

instaOrganizer(root, singleItem, singlePhoto)