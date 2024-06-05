#CODE EXPLANATION
'''
This script takes a folder of images (content) and an image (cover) and creates a new folder in which the content is distributed in sets of 10,
where the first image of each set is the cover image.
'''

#LIBRARY IMPORT
import os                           #Directory management
import shutil                       #Directory operations
import tkinter as tk
from tkinter import filedialog      #Directory and file searching


#FUNCTIONS DEFINITION
def CopyRename(image_path: str, destination_dir: str, new_name: str):
    #Variables
    old_name: str
    
    old_name = os.path.basename(image_path)
    shutil.copy(image_path, destination_dir)
    os.rename(os.path.join(destination_dir, old_name), os.path.join(destination_dir, new_name))

def CopyContent(content_dir: str, destination_dir: str):
    #Variables
    element: str
    files: list
    counter: int

    files = os.listdir(content_dir)                                 #Get the files in the directory
    files = files[:-1]                                              #Exclude the destiny directory
    files = sorted(files, key = lambda x : int(x.split('.')[0]))    #Order the file names
    counter = 1

    for element in files:
        #Excluding the non-image elements
        if not element.endswith('.png'):
            continue

        #Letting a space for the cover image
        if counter % PACK_LENGTH == 0:
            counter += 1
        
        CopyRename(os.path.join(content_dir, element), destination_dir, f'0{str(counter)}.png')
        counter += 1


def CopyCover(cover_path: str, destination_dir: str, quantity: int):
    #Variables
    pack:int = 0

    for pack in range(quantity):
        CopyRename(cover_path, destination_dir, f'0{str(pack * PACK_LENGTH)}.png')


def PackFiller(content_dir: str, cover_path: str):
    #Variables
    destination_dir: str
    cover_quantity: int
    
    os.mkdir(os.path.join(content_dir, DIR_NAME))
    destination_dir = os.path.join(content_dir, DIR_NAME)

    cover_quantity: int = (len(os.listdir(content_dir)) // PACK_LENGTH) + 1
    
    CopyContent(content_dir, destination_dir)
    CopyCover(cover_path, destination_dir, cover_quantity)

#Global variables
path: str
frontPage: str

#Global constants
DIR_NAME = 'Nueva Carpeta'
PACK_LENGTH = 10

root = tk.Tk()
root.withdraw()

path = filedialog.askdirectory()
path = os.path.abspath(path)

frontpage_path = filedialog.askopenfilename()
frontpage_path = os.path.abspath(frontpage_path)

PackFiller(path, frontpage_path)