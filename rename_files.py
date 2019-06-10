import os
def rename_files():
    #(1) get file names drom a folder
    file_list = os.listdir(r"C:\OOP\prank")
    saved_path = os.getcwd()
    print("current working directory is "+saved_path)
    os.chdir(r"C:\OOP\prank")
    #(2) for each file,rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
     os.chd
     
rename_files()
