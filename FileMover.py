import os
import shutil
import re, glob, os, time, datetime

file_extension = '.txt'
sourcepath = 'C:\\Users\\mhkhan\\Desktop\\test1'
sourcefiles = os.listdir(sourcepath)
destinationpath = 'C:\\Users\\mhkhan\\Desktop\\test2'
countFiles = 0

# for file in sourcefiles:
#     if file.endswith('.png'):
#         shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))

for folderName, subfolders, filenames in os.walk(sourcepath):

    print('The current folder is ' + folderName)
    sourcepath = folderName
    sourcefiles = os.listdir(sourcepath)

    for file in sourcefiles:
        if file.endswith(file_extension):
               # modifiedDate = os.path.getmtime(file)
                #year, month, day, hour, minute, second = time.localtime(modifiedDate)[:-3]
                #strModDate = ("%d%02d%02d" % (year, month, day))
                #newfileName = strModDate + '_' + file
                shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
                countFiles = countFiles + 1

        #print ('done!')

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        sourcepath = folderName+'\\'+subfolder
        sourcefiles = os.listdir(sourcepath)
        for file in sourcefiles:
                if file.endswith(file_extension):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
                    countFiles = countFiles + 1

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)


print ('total files moved: ' + str(countFiles))



# file renameing

#sourcepath = 'C:/docs/python/Humayun_Docs'
#sourcefiles = os.listdir(sourcepath)

def renamer(files, pattern, replacement):
    for pathname in glob.glob(files):
        basename= os.path.basename(pathname)
        new_filename= re.sub(pattern, replacement, basename)
        if new_filename != basename:
            os.rename(
              pathname,
              os.path.join(os.path.dirname(pathname), new_filename))

# rename("*.doc", r"^(.*)\.doc$", r"new(\1).doc")