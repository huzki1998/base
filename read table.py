import re
import pandas as pd

string ='幻想战刃技能持续时间提升50%暴击率，50%无视一击概率，持续5秒'
pattern = r"\d+"  # 匹配数字的正则表达式
matches =re.findall(pattern,string) # 在字符串中查找匹配项
numbers = [int(match) for match in matches]  # 将匹配到的字符串转换为整数
print(numbers)  # 输出结果