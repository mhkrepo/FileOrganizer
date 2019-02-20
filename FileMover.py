import os
import shutil
import re
import glob
import os
import time
import datetime

file_extension = '.txt'
sourcePath = 'C:\\Users\\mhkhan\\Desktop\\test1'
sourceFiles = os.listdir(sourcePath)
destinationPath = 'C:\\Users\\mhkhan\\Desktop\\test2'
countFiles = 0

# for file in sourcefiles:
#     if file.endswith('.png'):
#         shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))

for folderName, subFolders, fileNames in os.walk(sourcePath):

    print('The current folder is ' + folderName)
    sourcePath = folderName
    sourceFiles = os.listdir(sourcePath)

    for file in sourceFiles:
        if file.endswith(file_extension):
            # modifiedDate = os.path.getmtime(file)
            # year, month, day, hour, minute, second = time.localtime(modifiedDate)[:-3]
            # strModDate = ("%d%02d%02d" % (year, month, day))
            # newfileName = strModDate + '_' + file
            shutil.move(os.path.join(sourcePath, file), os.path.join(destinationPath, file))
            countFiles = countFiles + 1

        # print ('done!')

    for subFolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subFolder)
        sourcePath = folderName + '\\' + subFolder
        sourceFiles = os.listdir(sourcePath)
        for file in sourceFiles:
            if file.endswith(file_extension):
                shutil.move(os.path.join(sourcePath, file), os.path.join(destinationPath, file))
                countFiles = countFiles + 1

    for filename in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

print('total files moved: ' + str(countFiles))


# file renameing
# sourcepath = 'C:/docs/python/Humayun_Docs'
# sourcefiles = os.listdir(sourcepath)

def renamer(files, pattern, replacement):
    for pathname in glob.glob(files):
        basename = os.path.basename(pathname)
        new_filename = re.sub(pattern, replacement, basename)
        if new_filename != basename:
            os.rename(
                pathname,
                os.path.join(os.path.dirname(pathname), new_filename))

# rename("*.doc", r"^(.*)\.doc$", r"new(\1).doc")
