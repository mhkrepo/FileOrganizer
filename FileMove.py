import os
import shutil

file_extension = '.docx'
sourcePath = 'C:\\Users\\mhkhan\\Desktop\\Test'
destinationPath = 'C:\\Users\\mhkhan\\Desktop\\Test'
sourceFiles = os.listdir(sourcePath)
countFiles = 0

for (dirName, dirs, files) in os.walk(sourcePath):
    for file in files:
        if file.endswith(file_extension):
            theFile = os.path.join(dirName, file)
            sourceFile = os.path.join(sourcePath, file)
            destinationFile = os.path.join(destinationPath, file)
            shutil.move(theFile, destinationFile)
print('done')


