# import pandas as pd
#
# # 读取原始文件
# df = pd.read_excel('your_file.xlsx', header=None)
#
# # 获取第一列的数据
# col1 = df.iloc[:, 0]
#
# # 将第一列中的每个元素进行处理
# col2 = col1.apply(lambda x: [round(2 * float(i), 2) if float(i) != round(float(i)) else int(2 * float(i)) for i in x.strip('[]').split(',')])
#
# # 将处理后的数据存放到第二列
# df.loc[:, 1] = col2
#
# # 去掉逗号后面的空格
# df[1] = df[1].apply(lambda x: [str(i).replace(', ', ',') for i in x])
#
# # 将第二列重新赋值为修改后的Series对象
# df.iloc[:, 1] = df[1]
#
# # 去掉第二列中的'和'和','
# df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: [i for i in x if i not in ['和', ',']])
#
# # 将第二列中的每个元素用逗号连接起来，并添加[]符号
# df.loc[:, 2] = df.iloc[:, 1].apply(lambda x: '[' + ','.join(x) + ']')
#
# # 删除第二列
# df.drop(columns=[1], inplace=True)
#
# # 保存修改后的文件
# df.to_excel('your_file.xlsx', index=False, header=False)


import pandas as pd

# 读取原始文件
df = pd.read_excel('your_file.xlsx', header=None)

# 获取第一列的数据
col1 = df.iloc[:, 0]

# 将第一列中的每个元素进行处理，并存放到新的一列
df.loc[:, 1] = col1.apply(lambda x: ','.join([str(round(2 * float(i), 2)) if float(i) != round(float(i)) else str(int(2 * float(i))) for i in x.strip('[]').split(',')]))


# 保存修改后的文件
df.to_excel('your_file.xlsx', index=False, header=False)
















