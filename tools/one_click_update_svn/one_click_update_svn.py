import subprocess

# 读取路径文件
with open('path_list.txt', 'r', encoding='utf-8') as f:
    paths = f.read().splitlines()

# 遍历路径并执行svn命令
for path in paths:
    command = ['svn', 'update', path]
    subprocess.run(command, check=True)
