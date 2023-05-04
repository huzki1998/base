# This is the code for copying specific files from a directory to a destination directory:

# 1. Define the source and destination directories.
# 2. Check if the destination directory exists. If not, create it using `os.makedirs()`.
# 3. Check if the source directory exists. If not, print an error message and exit.
# 4. Read the list of filenames to copy from the `list.txt` file using `open()`.
# 5. Traverse through the source directory and all its subdirectories using `os.walk()`.
# 6. For each file in the directory, check if its name is in the list of filenames to copy.
# 7. If the file name is in the list, construct the source and destination file paths using `os.path.join()`.
# 8. Copy the file from the source path to the destination path using `shutil.copy()`.
# 9. If the copy is successful, print a success message. Otherwise, print an error message with the reason for the failure.

# The code essentially copies a list of specified files from a source directory to a destination directory, and creates the destination directory if it does not exist.


import os
import shutil

location_path="D:\\tianshi\\domestic_release\\domestic_release\\tables"
des_dir="C:\\Users\\huzhk\\Desktop\\copy_file"

# Check if the target directory exists. If not, create it.
if not os.path.isdir(des_dir):
    # If the directory does not exist, create it and all its parent directories using os.makedirs()
    os.makedirs(des_dir)
    print('directory has been created：{}'.format(des_dir))

# Check if the source directory exists.
if not os.path.isdir(location_path):
    print('Source directory does not exist')
    exit()

# Read the list.txt file to get the list of filenames to copy.
with open('list.txt', 'r', encoding='utf-8') as f:
    file_list = f.read().splitlines()

# Traverse through the specified directory and all its subdirectories.
for root, dirs, files in os.walk(location_path):
    for file_name in files:
        # If the file name is in the list, copy it to the target directory.
        if file_name in file_list:
            # Construct the source and destination file paths.
            src_path = os.path.join(root, file_name)
            dst_path = os.path.join(des_dir, file_name[:-5] + "-new.xlsx")
            # Copy the file.
            try:
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                # The shutil.copy() method can preserve file metadata such as permissions and creation time.
                # If metadata preservation is not necessary, shutil.copy2() can also be used.
                shutil.copy(src_path, dst_path)
                print('success copied %s' % file_name)
            except Exception as e:
                print('copy failed %s reason：%s' % (file_name, str(e)))