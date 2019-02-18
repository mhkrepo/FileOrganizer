import os,time, datetime

import shutil
import re, glob, os

file_extension = '.docx'
sourcepath = 'C:\\Users\\mhkhan\\Desktop\\Test'
destinationpath = 'C:\\Users\\mhkhan\\Desktop\\Test'

sourcefiles = os.listdir(sourcepath)

countFiles = 0

from os.path import join

for (dirname, dirs, files) in os.walk(sourcepath):
   for file in files:
       if file.endswith(file_extension):
            thefile = os.path.join(dirname,file)
            sourceFile = os.path.join(sourcepath,file)
            destinationFile = os.path.join(destinationpath,file)
            shutil.move(thefile,destinationFile)
print('done')


