## 项目介绍

本项目是一个用于自动翻译Obsidian的插件界面的Python脚本。通过调用正则表达式和翻译api，可以将插件中的大部分英文文本转换为中文

## 为什么写这个项目？

因为我看到很多插件都是英文的，对中文不友好，所以于是写了这个小项目

本人并不是专业的python开发者(在路上)，有问题还请大家提出意见！

> 可以的话，star 支持一下！！！

## 注意

- 翻译之前请先备份好之前的文件！！！

- 翻译之前请先备份好之前的文件！！！

- 翻译之前请先备份好之前的文件！！！

我测试了好久，暂时没有发现问题

但部分内容可能不会被翻译到！

但还是建议使用之前先备份好原文件！
可能会出现未知错误！！！

## 更新日志
1. v1.1    2024.04.11
- 增加 *小牛翻译*
- 删除代码报错`sys.stdout.reconfigure(encoding='utf-8')`
- 增加对`appendText`函数中的字符串的翻译
- 优化各个匹配函数，增加判断条件，减少替换次数
- 优化翻译输出信息

## 安装与运行

### 环境要求

确保你已经安装了Python 3版本。本项目在Python 3.7以上进行测试。
安装`requests`,`hashlib`等库

### 下载并配置

1. 在GitHub上克隆或下载此项目到本地目录。
2. 打开`config.py`文件，并填写正确的appid密钥和URL、文件路径、(开始结束行可以不替换,另外使用百度翻译或者gpt翻译请记得设置True/False)
3. 安装依赖库`requests`  `hashlib` ,执行以下命令:

```bash
pip install -r requirements.txt
```

### 运行

在命令行中进入项目根目录，执行以下命令启动程序：
(pycharm直接运行app.py)

```bash
python app.py
```

### 文件说明

```
文件结构
├── app.py
├── config.py
├── re_API.py
├── translate_API.py
└── config.json
```

- app.py：主程序文件
- config.py：从config.json文件中读取配置数据
- re_API.py：提供正则表达式匹配和替换功能的函数
- translate_API.py：调用翻译API进行文本翻译的模块，支持百度翻译和GPT两种方式
- config.json：配置信息文件
## 功能说明

### 支持以下函数中的字符串：
支持对js代码中的多种字符串模式进行匹配和替换，包括：
- `setName`函数中的字符串
- `setDesc`函数中的字符串
- `description`字段的值
- `data-description`属性的值
- `HTML li`标签中的文本内容
- `HTML p`标签中的纯英文文本内容
- `info`字段的值
- `addDesc`字段的值
- `appendText`字段的值

支持百度翻译，小牛翻译和GPT三种翻译服务。你可以在config.json文件中选择使用的翻译服务。

### 未来计划
- [ ] 支持有道翻译
- [ ] 打包程序，无需py环境
- [ ] 等待添加......


## 常见问题与解决办法
### 1. Q: 我没有百度/小牛翻译/openai密钥怎么办？

A: 你需要申请百度翻译、小牛翻译或者OpenAI API的密钥。具体步骤如下：

>百度翻译/小牛翻译API
访问 百度翻译/小牛翻译开放平台。
注册并登录你的账号。
创建应用，获取API密钥。

>OpenAI API
*支持类似openai请求方式的api*
### 2. Q: 翻译过程中出现错误怎么办？

A: 如果你在运行程序时遇到错误，请检查以下事项：

检查是否正确填写了config.json文件中的API密钥和URL。
检查输入的JavaScript文件路径和输出目录是否存在且可写。
检查网络连接是否正常。
确保每个路径的`\`之前再加一个`\`

### 3.出现问题汇总
(1). 出现with open(js_file_path, 'r', encoding='utf-8') as file:
OSError: [Errno 22] Invalid argument:可能是文件路径包含\t,\n等转义字符，直接在`\t`等转义字符之间加上 `斜杠\`,如：` \\t `

如果你仍然无法解决问题，请提交issues

作者python水平有限，欢迎贡献代码和提出改进意见！ 

最后，有问题，请联系我！
