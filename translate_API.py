# -*- coding: utf-8 -*-
# 该脚本用于调用翻译API进行文本翻译
# 需要安装requests库，使用pip install requests命令进行安装
import json
import random
from hashlib import md5
import requests
# from config import config_data
import json
# config_data=[]
with open('config.json', 'r',encoding='utf-8') as file:
    config_data = json.load(file)

# 定义生成MD5签名的函数
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def Baidu_Translate(query):
    # 设置百度翻译API的appid和appkey
    baidu_appid = config_data['baidu_appid']
    baidu_appkey = config_data['baidu_appkey']

    # 设置源语言和目标语言
    from_lang = 'en'
    to_lang = 'zh'

    # 百度翻译API地址
    baidu_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    # 生成随机的salt值
    salt = random.randint(24685, 65536)
    # 生成签名
    sign = make_md5(baidu_appid + query + str(salt) + baidu_appkey)

    # 设置请求头和请求参数
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': baidu_appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # 发送POST请求
    r = requests.post(baidu_url, params=payload, headers=headers)

    # 解析返回结果
    result = r.json()
    if 'trans_result' in result and result['trans_result']:
        translated_text = result['trans_result'][0].get('dst', 'Translation not found')
        print(f'----{query}翻译成功-----')
    else:
        translated_text = query  # 如果没有翻译结果，就使用原始文本

    return translated_text

def XiaoniuTranslate(query):
    # 构建请求的URL和参数
    xiaoniu_url = 'http://api.niutrans.com/NiuTransServer/translation'
    params = {
        "from": "en",
        "to": "zh",
        "apikey": config_data["xiaoniu_apikey"],
        "src_text": query
    }

    # 发送POST请求
    response = requests.post(xiaoniu_url, data=params)

    # 解析响应内容
    res_dict = response.json()
    if "tgt_text" in res_dict:
        translated_text = res_dict['tgt_text']
        print(f'---{query} ✅ 翻译成功------------')
    else:
        print(f'---{query} ❌ 翻译失败------------')
        translated_text = query

    return translated_text

def GPT_Translate(query):
    base_url = config_data['base_url']
    # 替换为你的OpenAI API密钥
    api_key = config_data['api_key']
    # 设置请求URL和头信息
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 定义要发送的数据
    data = {
        "model": config_data['model'],
        "messages": [{"role": "user", "content": "你多大了"}]  # 可以在这里添加你的输入
    }
    prompt = config_data['translate_prompt']
    data["messages"][0]["content"] = prompt + query  # 提示用户输入问题
    # 发送POST请求
    response = requests.post(base_url, headers=headers, data=json.dumps(data))
    # 解析和打印响应内容
    if response.status_code == 200:
        response = response.json()
        response_text = response["choices"][0]["message"]["content"]
        print(f'---{query}翻译成功------------')
        return response_text
    else:
        return query


def Translate_words(query):
    if config_data['is_use_Baidu']=="True":
        return Baidu_Translate(query)
    elif config_data['is_use_GPT']=="True":
        return GPT_Translate(query)
    elif config_data['is_use_Xiaoniu']=="True":
        return XiaoniuTranslate(query)
    else:
        return query

# print(type(config_data['is_use_GPT']))
# print(Translate_words('how are you,i miss you，"Miss"'))
# -----------------------------------------------------

