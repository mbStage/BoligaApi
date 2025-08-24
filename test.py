import os 

IMAGE_FOLDERS = "C:\\Users\\falds\\Documents\\Martin\\Git\\BoligaApi\\images"

files = []
for IMAGE_FOLDER in os.listdir(IMAGE_FOLDERS) :
    #print(IMAGE_FOLDER)
    files.append([f for f in os.listdir(f'{IMAGE_FOLDERS}\\{IMAGE_FOLDER}') if os.path.isfile(os.path.join(f'{IMAGE_FOLDERS}\\{IMAGE_FOLDER}', f))])
print(files[:5])