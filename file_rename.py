import os
import re
def file_rename():
    file_list = os.listdir(r"/Users/rutuzoa/Documents/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is" + saved_path)
    os.chdir(r"/Users/rutuzoa/Documents/prank")
    saved_path_1 = os.getcwd()
    print("Next working directory is" + saved_path_1)
    for file_name in file_list:
        os.rename(file_name, file_name.translate( None,"0123456789"))
    os.chdir(saved_path)
file_rename()
