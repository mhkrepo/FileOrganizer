import os,time, datetime

import shutil
import re, glob, os
from os.path import join

file_extension = '.pdf'
sourcePath = 'C:\\Users\\mhkhan\\Desktop\\pdf'
sourceFiles = os.listdir(sourcePath)
#destinationPath = 'C:\\Users\\mhkhan\\Desktop\\pdf1'
counter = 0


for (dirName, dirs, files) in os.walk(sourcePath):
    for file in files:

        if file.endswith(file_extension):
            OldFileName = os.path.join(dirName, file)
            print(OldFileName)
            #sourceFile = os.path.join(sourcePath, theFile)
            #destinationFile = os.path.join(destinationPath, theFile)
            #shutil.move(sourceFile, destinationFile)
            modifiedDate = os.path.getmtime(OldFileName)
            year, month, day, hour, minute, second = time.localtime(modifiedDate)[:-3]
            strModDate = ("%d%02d%02d" % (year, month, day))
            #newfileName = strModDate + '_' + file

            NeFileName = str(strModDate)+'_'+file
            NewFileName = os.path.join(dirName, NeFileName)
            os.rename(OldFileName, NewFileName)
            counter = counter + 1

print("Successfully renamed.")

# def renamer(files, pattern, replacement):
#     for pathname in glob.glob(files):
#         basename = os.path.basename(pathname)
#         new_filename = re.sub(pattern, replacement, basename)
#         if new_filename != basename:
#             os.rename(pathname,os.path.join(os.path.dirname(pathname), new_filename))