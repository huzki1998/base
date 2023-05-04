import subprocess

# Read the path file
with open('path_list.txt', 'r', encoding='utf-8') as f:
    paths = f.read().splitlines()

#  Traverse the paths and execute SVN commands
for path in paths:
    command = ['svn', 'update', path]
    subprocess.run(command, check=True)
