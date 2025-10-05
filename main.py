from pathlib import Path

from pato import patoOrganizer
from instagram import instaOrganizer

def main():
    
    choice = input("What Organizer would you like to use?").lower()
    
    if choice == 'pato':
        pato.patoOrganizer()
        
    elif choice == 'instagram':
        instagram.instaOrganizer()
   
    else:
        print("Invalid Choice. Exiting...")
        
        
if __name__ in main:
    main()