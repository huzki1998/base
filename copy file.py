# This Python script reads the target directory and the list of filenames to copy from two separate text files (des.txt and list.txt, respectively).
# It then walks through the directory and its subdirectories, looking for files with names that match the ones in the list. For each matching file, it constructs the source and destination paths and copies the file using the shutil.copy() method.
#
# The script also creates a new file name for the copied file by appending the suffix "-new.xlsx" to the original file name, before the extension. This means that if a file in the list is named "file.xlsx", the copied file will be named "file-new.xlsx".
#
# The script checks if the destination directory exists and if not, prints an error message and exits. If a file cannot be copied for any reason, the script prints an error message indicating the file name and the reason for the failure.
#
# Overall, the script is a useful tool for copying a specific list of files from a directory and its subdirectories.


import os
import shutil

# Read the des.txt file to get the target directory.
with open('des.txt', 'r', encoding='utf-8') as f:
    des_dir = f.read().strip()

# Check if the target directory exists.
if not os.path.isdir(des_dir):
    print('directory doesn\'t exists')
    exit()

# Read the list.txt file to get the list of filenames to copy.
with open('list.txt', 'r', encoding='utf-8') as f:
    file_list = f.read().splitlines()

# Traverse through the specified directory and all its subdirectories.
for root, dirs, files in os.walk(des_dir):
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
                print('success %s' % file_name)
            except Exception as e:
                print('success %s fail：%s' % (file_name, str(e)))

