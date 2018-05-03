import os

# path to folder containing files to be renamed
file_path = ""

def rename_files():
    # list all files in folder
    file_list = os.listdir(file_path)
    print(file_list)

    # rename each file
    os.chdir(file_path)
    for file_name in file_list:
        # in this case, strip all digits from filenames
        os.rename(file_name, file_name.translate(None, "0123456789"))
    print(file_list)

rename_files()
