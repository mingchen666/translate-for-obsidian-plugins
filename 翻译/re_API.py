# -*- coding: utf-8 -*-


import re
import sys

from translate_API import Translate_words


sys.stdout.reconfigure(encoding='utf-8')
# 定义要查找和替换的字符串模式addDesc，setPlaceholder,setButtonText,setTooltip
addDesc_pattern = re.compile(r"addDesc\(['\"]([^'\"]*)['\"]\)")
setName_pattern = re.compile(r"setName\(['\"]([^'\"]*)['\"]\)")
setDesc_pattern = re.compile(r"setDesc\(['\"]([^'\"]*)['\"]\)")
description_pattern = re.compile(r'\bdescription:\s*["\']([^"\']+?)["\']')
data_description_pattern = re.compile(r'data-description="([^"]*)"')
appendtText_pattern = re.compile(r"appendText\(['\"]([^'\"]*)['\"]\)")
addDesc_pattern = re.compile(r"addDesc\(['\"]([^'\"]*)['\"]\)")
# 匹配setName并且替换
def matches_setName(old_str_text, setName_pattern):
    """
    :param old_str_text: 原文本字符串
    :param new_str_text: 翻译后的文本字符串
    :return: 翻译后的文本字符串
    """

    # 判断字符串是否为空
    if old_str_text:
        matches = setName_pattern.findall(old_str_text)
        new_str_text = old_str_text
        for match in matches:
            translated_param = Translate_words(match)  # 假设这是一个翻译函数
            # 修改替换逻辑，同时考虑单引号和双引号
            new_str_text = new_str_text.replace(f'setName("{match}")', f'setName("{translated_param}")')
            new_str_text = new_str_text.replace(f"setName('{match}')", f"setName('{translated_param}')")
        # print('！！！---单个setname/decs替换成功')
        return new_str_text
    else:
        return old_str_text

# 匹配和setDecs并且替换
def matches_setDesc(old_str_text, setDesc_pattern):
    """
    :param old_str_text: 原文本字符串
    :param new_str_text: 翻译后的文本字符串
    :return: 翻译后的文本字符串
    """

    # 判断字符串是否为空
    if old_str_text:
        matches = setDesc_pattern.findall(old_str_text)
        new_str_text = old_str_text
        for match in matches:
            translated_param = Translate_words(match)  # 假设这是一个翻译函数
            # 修改替换逻辑，同时考虑单引号和双引号
            new_str_text = new_str_text.replace(f'setDesc("{match}")', f'setDesc("{translated_param}")')
            new_str_text = new_str_text.replace(f"setDesc('{match}')", f"setDesc('{translated_param}')")
        # print('！！！---单个setname/decs替换成功')
        return new_str_text
    else:
        return old_str_text

def matches_appendText(old_str_text, appendText_pattern):
    """
    :param old_str_text: 原文本字符串
    :param new_str_text: 翻译后的文本字符串
    :return: 翻译后的文本字符串
    """

    # 判断字符串是否为空
    if old_str_text:
        matches = appendText_pattern.findall(old_str_text)
        new_str_text = old_str_text
        for match in matches:
            translated_param = Translate_words(match)  # 假设这是一个翻译函数
            # 修改替换逻辑，同时考虑单引号和双引号
            new_str_text = new_str_text.replace(f'appendText("{match}")', f'appendText("{translated_param}")')
            new_str_text = new_str_text.replace(f"appendText('{match}')", f"appendText('{translated_param}')")
        # print('！！！---单个setname/decs替换成功')
        return new_str_text
    else:
        return old_str_text
def matches_addDesc(old_str_text, addDesc_pattern):
    """
    :param old_str_text: 原文本字符串
    :param new_str_text: 翻译后的文本字符串
    :return: 翻译后的文本字符串
    """
    # 判断字符串是否为空
    if old_str_text:
        matches = addDesc_pattern.findall(old_str_text)
        new_str_text = old_str_text
        for match in matches:
            translated_param = Translate_words(match)  # 假设这是一个翻译函数
            # 修改替换逻辑，同时考虑单引号和双引号
            new_str_text = new_str_text.replace(f'addDesc("{match}")', f'addDesc("{translated_param}")')
            new_str_text = new_str_text.replace(f"addDesc('{match}')", f"addDesc('{translated_param}')")
        # print('！！！---单个adddecs替换成功')
        return new_str_text
    else:
        return old_str_text

# 《未实现》---同时匹配setName和setDecs并且替换
def matches_both_set(input_text):
    if input_text:
        def replace_param(match):
            if match.group(1):
                param = match.group(1)
                translated_param = Translate_words(param)
                return f'setName("{translated_param}")'
            else:
                param = match.group(2)
                translated_param = Translate_words(param)
                return f'setDecs("{translated_param}")'

        result = re.sub(r'setName\("([^"]+)"\)|setDesc\("([^"]+)"\)', replace_param, input_text)
        # print('---全部匹配成功')
        return result
    else:
        return input_text


# 匹配description并且替换
def matches_description(old_str_text):
    if old_str_text:
        description_pattern = re.compile(r'\bdescription:\s*"(.*?)"')  # 更新正则表达式模式，匹配单词边界
        match = description_pattern.search(old_str_text)
        if match:
            translated_param = Translate_words(match.group(1))
            replaced_text = f'description: "{translated_param}"'
            new_str_text = description_pattern.sub(replaced_text, old_str_text, 1)
            # print('*******description 替换成功')
            return new_str_text
        else:
            return old_str_text
    else:
        return old_str_text

# 匹配data-description并且替换
def matches_data_description(old_str_text):
    if old_str_text:

        match = data_description_pattern.search(old_str_text)
        if match:
            translated_param = Translate_words(match.group(1))
            replaced_text = f'data-description="{translated_param}"'
            new_str_text = data_description_pattern.sub(replaced_text, old_str_text, 1)
            return new_str_text
        else:
            return old_str_text
    else:
        return old_str_text
te1='data-description="Select a model to use with Smart Chat."'
print(matches_data_description(te1))

# 有问题。待修改
def matches_li_tag(old_str_text):
    if old_str_text:
        li_pattern = re.compile(r'<li>(.*?)</li>')
        def replace_fn(match):
            translated_match = Translate_words(match.group(1))
            return f'<li>{translated_match}</li>'
        new_str_text = li_pattern.sub(replace_fn, old_str_text)
        return new_str_text
    else:
        return old_str_text
te2='<li>Using a model that is too large for your computer may cause errors. For instance, the Jina-small-4K model works on a Mac M2 8GB, while the Jina-small-8K model fails.</li>'
# print(matches_li_tag(te2))
# p标签里面纯英文
def matches_p_tag(old_str_text):
    if old_str_text:
        p_pattern = re.compile(r'<p>([A-Za-z\s,.!?\'\"]+)</p>')
        def replace_fn(match):
            translated_match = Translate_words(match.group(1))
            return f'<p>{translated_match}</p>'
        new_str_text = p_pattern.sub(replace_fn, old_str_text)
        return new_str_text
    else:
        return old_str_text
te3=' "<p>" + ScTranslations[this.plugin.settings.language].initial_message + "</p>";'
# print(matches_p_tag(te3))
# info测试匹配
def matches_info(old_str_text):
    if old_str_text:
        description_pattern = re.compile(r'info:"(.*?)"')
        match = description_pattern.search(old_str_text)
        if match:
            translated_param = Translate_words(match.group(1))
            replaced_text = f'info:"{translated_param}"'
            new_str_text = description_pattern.sub(replaced_text, old_str_text, 1)
            # print('*******description 替换成功')
            return new_str_text
        else:
            return old_str_text
    else:
        return old_str_text
# 《未实现》---匹配title并且替换
def matches_title(old_str_text):
    if old_str_text:
        title_pattern = re.compile(r'\btitle:\s*"(.*?)"')  # 更新正则表达式模式，匹配单词边界
        match = description_pattern.search(old_str_text)
        if match:
            translated_param = Translate_words(match.group(1))
            replaced_text = f'description: "{translated_param}"'
            new_str_text = description_pattern.sub(replaced_text, old_str_text, 1)
            print('*******title 替换成功')
            return new_str_text
        else:
            return old_str_text
    else:
        return old_str_text


def read_js_file(js_file_path: str, new_js_file_name: str,start_line: int, end_line: int):
    """
    :param js_file_path: js文件路径
    :param start_line: 开始行数
    :param end_line:
    """
    with open(js_file_path, 'r', encoding='utf-8') as file:
        count = 0
        lines = file.readlines()
        # lines = [line.strip() for line in lines]
        if start_line is not None and end_line is not None:
            lines = lines[start_line - 1: end_line]

        with open(new_js_file_name, 'w', encoding='utf-8') as f:
            for line in lines:
                decoded_line1 = line.rstrip()
                decoded_line2 = matches_setName(decoded_line1, setName_pattern)
                decoded_line3 = matches_setDesc(decoded_line2, setDesc_pattern)
                # print(matches_both_set(decoded_line2))
                decoded_line4 = matches_description(decoded_line3)
                decoded_line5=matches_info(decoded_line4)
                # decoded_line6 = matches_li_tag(decoded_line5)
                decoded_line7 = matches_p_tag(decoded_line5)

                decoded_line8 = matches_appendText(decoded_line7,appendtText_pattern)
                decoded_line9 = matches_addDesc(decoded_line8, addDesc_pattern)
                new_line = matches_data_description(decoded_line9)
                # print(new_line)
                if new_line is not None:
                    f.write(new_line + '\n')
    print('============< 翻译完成 >============')

