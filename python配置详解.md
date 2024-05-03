
# Python环境/配置说明文档

## 安装python
> python安装教程 自行百度搜索


## 查看版本

### 查看Python版本

```bash
python --version
```

### 查看pip版本


```bash
pip --version
```


## 使用pip安装包

pip安装Python包的通用命令是：

```bash
pip install package_name
```

其中`package_name`是要安装的包的名称。例如，要安装`numpy`包，可以使用：

```bash
pip install numpy
```

## 使用国内镜像源（通用，加快包的下载速度）

为了加速包的下载速度，可以使用国内镜像源。以下是一些常用的国内镜像源：

- 阿里云：https://mirrors.aliyun.com/pypi/simple/
- 豆瓣：https://pypi.douban.com/simple/
- 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/

1. 要使用国内镜像源，可以在命令行中输入以下命令（以阿里云为例）：

```bash
pip install package_name -i https://mirrors.aliyun.com/pypi/simple/
```
这样即可使用国内镜像源进行安装。

2. 一劳永逸，或者可以通过修改`pip.conf`文件来永久更改镜像源。在用户目录下创建或修改`pip.conf`文件，并添加以下内容（以阿里云为例）：

```
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
```

保存文件后，pip将自动使用指定的镜像源进行安装。

