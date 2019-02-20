import os,time, datetime
import shutil
import re, glob, os
from os.path import join

#def file_rename():
#def file_move():
#rename


# appending  date to file name

def rename_file(dir_path, file_name):
            old_file_name = os.path.join(dir_path, file_name)
            print(old_file_name)
            file_modified_date = os.path.getmtime(old_file_name)
            year, month, day, hour, minute, second = time.localtime( file_modified_date)[:-3]
            str_file_modified_date = ("%d%02d%02d" % (year, month, day))
            new_file_name = str(str_file_modified_date)+'_'+file_name
            final_new_file_name = os.path.join(dir_path, new_file_name)
            os.rename(old_file_name, final_new_file_name) #rename file with date
            print("Successfully renamed.")


def main():

    fn_ = '10-Best-VIM-Cheat-Sheet-01.pdf'
    dp_ = 'C:\\Users\\mhkhan\\Desktop\\Test\\test'

    rename_file(dp_, fn_)

main()