import os
path = ("/prank")
os.chdir(path)

def rename_files():
    #(1) get names from  th folder
    file_list = os.listdir("/prank")
    print (file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is:"+ saved_path)
    os.chdir("/prank")
    #(2) for each file, Change the name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.listdir(saved_path)

rename_files()   