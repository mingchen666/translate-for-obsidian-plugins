# 从 JSON 文件中读取数据
import json

with open('config.json', 'r',encoding='utf-8') as file:
    config_data = json.load(file)
# print(config_data)