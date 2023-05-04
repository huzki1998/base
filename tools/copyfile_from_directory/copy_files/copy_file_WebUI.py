from flask import Flask, render_template, request
import os
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def copy_files():
    location_path = request.form['source_dir']
    des_dir = request.form['des_dir']
    file_list = request.form['file_list'].splitlines()

    if not os.path.isdir(des_dir):
        os.makedirs(des_dir)
        print('目标目录已创建：{}'.format(des_dir))

    if not os.path.isdir(location_path):
        print('源目录不存在')
        exit()

    file_copied = []
    for root, dirs, files in os.walk(location_path):
        for file_name in files:
            if file_name in file_list:
                src_path = os.path.join(root, file_name)
                dst_path = os.path.join(des_dir, file_name[:-5] + "-new.xlsx")
                try:
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    shutil.copy(src_path, dst_path)
                    file_copied.append(file_name)
                except Exception as e:
                    print('无法复制文件 {} 原因：{}'.format(file_name, str(e)))

    return render_template('index.html', message='以下文件已成功复制：{}'.format(file_copied))

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
