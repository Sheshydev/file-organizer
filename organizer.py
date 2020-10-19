import os

directories = []
dirNames = [['Documents', 0], ['Pictures', 0], ['Videos', 0], ['Audio', 0], ['Zip files', 0], ['Miscellaneous', 0]]
dirTypeAssoc = [['Documents', '.pdf', '.doc', '.docx', '.txt','.xlsx'], 
    ['Pictures', '.jpeg', '.png', '.gif'], 
    ['Videos', '.mp4', '.wav'],
    ['Audio', '.mp3'],
    ['Zip files', '.zip']
]

def createDir(dirName, dirCount):
    #takes a directory name and creates it 
    if os.path.isdir(f'.\{dirName}'):
        dirCount += 1
        while os.path.isdir(f'.\{dirName}({dirCount})'):
            #will number the directory if another directory of the same name is used
            dirCount += 1
    try:
        if (dirCount > 0):
            os.mkdir(f'.\{dirName}({dirCount})')
            directories.append(f'.\{dirName}({dirCount})')
        else:
            os.mkdir(f'.\{dirName}')
            directories.append(f'.\{dirName}')
    except OSError:
        print(f'could not create {dirName} file')
        exit()
    else:
        print(f'{dirName} file created!')
    return dirCount

def moveFiles(file):
    reverseDotIndex = len(file) - file.rfind('.')
    fileType = file[-reverseDotIndex:len(file)]
    destDir = [x for x in dirTypeAssoc if fileType in x]
    if destDir:
        dirCount = [x for x in dirNames if destDir[0][0] in x][0]
        try:
            if dirCount[1] > 0:
                os.rename(f'.\{file}', f'.\{destDir[0][0]}({dirCount[1]})\{file}')
            else:
                os.rename(f'.\{file}', f'.\{destDir[0][0]}\{file}')
        except OSError:
            print("unable to move file ")
        else:
            print(f"moved file {file}!")
    else:
        destDir = "Miscellaneous"
        dirCount = [x for x in dirNames if destDir in x][0]
        print(f'.\{file}', f'.\destDir({dirCount[1]})\{file}')
        try:
            if dirCount[1] > 0:
                os.rename(f'.\{file}', f'.\{destDir}({dirCount[1]})\{file}')
            else:
                os.rename(f'.\{file}', f'.\{destDir}\{file}')
        except OSError:
            print("unable to move file ")
        else:
            print(f"moved file {file}!")

def main():
    for dirName in dirNames:
        dirName[1] = createDir(dirName[0], dirName[1])

    files = [file for file in os.listdir('.') if os.path.isfile(file)]
    files.remove('organizer.py')
    for file in files:
        moveFiles(file)
    
main()
            
            
