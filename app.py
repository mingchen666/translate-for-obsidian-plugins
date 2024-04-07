# -*- coding: utf-8 -*-
"""
app.py

这是一个为obsidian插件进行翻译的脚本

Author: 小罗
Date: 2024-03-28
Version: 1.0.0

"""

from pathlib import Path

from re_API import *
from config import config_data
# 设置标准输出编码为UTF-8
# sys.stdout.reconfigure(encoding='utf-8')

# 定义要查找和替换的字符串模式
setName_pattern = re.compile(r'setName\(["\']([^"\']+?)["\']\)')
setDesc_pattern = re.compile(r'setDesc\(["\']([^"\']+?)["\']\)')

description_pattern = re.compile(r'\bdescription:\s*["\']([^"\']+?)["\']')


# 调用并指定参数
js_file_path = Path(config_data['js_file_path'])
new_js_file = js_file_path.parent / 'main_cn.js'
# new_js_file = config_data['new_js_file']
start_line = 1
end_line = 1000000







if '__main__'==__name__:
    print('运行成功！版本号:1.0')
    read_js_file(js_file_path, new_js_file, start_line, end_line)