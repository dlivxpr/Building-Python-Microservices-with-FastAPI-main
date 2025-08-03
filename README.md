


# 使用 FastAPI 构建 Python 微服务

<a href="https://www.packtpub.com/product/building-python-microservices-with-fastapi/9781803245966?utm_source=github&utm_medium=repository&utm_campaign=9781803245966"><img src="https://static.packt-cdn.com/products/9781803245966/cover/smaller" alt="Building Python Microservices with FastAPI" height="256px" align="right"></a>

## 📚 关于本仓库

这是 [使用 FastAPI 构建 Python 微服务](https://www.packtpub.com/product/building-python-microservices-with-fastapi/9781803245966?utm_source=github&utm_medium=repository&utm_campaign=9781803245966) 一书的学习记录仓库。

**原作者：** Sherwin John Calleja Tragura  
**出版社：** Packt Publishing  
**原始仓库：** [PacktPublishing/Building-Python-Microservices-with-FastAPI](https://github.com/PacktPublishing/Building-Python-Microservices-with-FastAPI)

### 🎯 仓库目的

本仓库是基于原作者代码的个人学习记录，用于：
- 📖 跟随书籍内容学习 FastAPI 微服务开发
- 💻 实践书中的代码示例和项目
- 📝 记录学习过程中的心得和笔记
- 🔧 在原有代码基础上进行实验和改进

> **声明：** 本仓库仅用于个人学习目的，所有原始代码版权归原作者和 Packt Publishing 所有。

**从设计概念到基础设施，构建安全、可扩展且结构化的 Python 微服务**

## 关于本书
FastAPI 是一个基于异步服务器网关接口（ASGI）的框架，可以帮助构建现代、可管理且快速的微服务。由于其异步核心平台，这个基于 ASGI 的框架在性能、可靠性和可扩展性方面提供了比基于 WSGI 的 Django 和 Flask 更好的选择。当使用 Python、Flask 和 Django 微服务时，您将能够通过这本构建无缝可管理和快速微服务的实用指南来应用您的知识。

本书涵盖以下精彩特性：
* 使用 FastAPI 框架的基本组件理解、定位和实现 REST API
* 使用内置的 pydantic 模块和 asyncio 支持构建异步和同步 REST 服务
* 使用 FastAPI 支持的功能创建小规模和大规模微服务应用程序
* 使用框架构建事件驱动和消息驱动的应用程序
* 使用关系型和 NoSQL 数据库创建异步和同步数据层

如果您觉得这本书适合您，请立即获取您的[副本](https://www.amazon.com/dp/1803245964)！

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## 使用说明和导航
所有代码都按文件夹组织。例如，Chapter01。

代码示例如下：
```
@app.get("/ch01/login/")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
```

**本书适合以下读者：**

本书适合 Python Web 开发者、高级 Python 用户，以及使用 Flask 或 Django 的后端开发者，他们希望学习如何使用 FastAPI 框架来实现微服务。熟悉 REST API 和微服务的读者也将从本书中受益。本书的某些部分包含通用概念、流程和说明，中级开发者和 Python 爱好者也能够理解。

使用以下软硬件列表，您可以运行本书中的所有代码文件（第 1-11 章）。

### 软硬件列表

| 章节     | 所需软件                            | 所需操作系统                                     |
| -------- | ------------------------------------| -------------------------------------------------|
| 1-11     | Python 3.8 或 3.9                   | Windows、macOS 或 Linux                         |
| 1-11     | PostgreSQL 13.x                     | 任何操作系统的 64 位版本                         |
| 1-11     | VS Code 编辑器                      | 任何操作系统的最新版本                           |
| 1-11     | MongoDB 5.x                         | 任何操作系统的 64 位版本                         |
| 1-11     | Mongo Database Tools                | 任何操作系统的 64 位版本                         |
| 1-11     | Mongo Compass                       | 任何操作系统的 64 位版本                         |
| 1-11     | RabbitMQ                            | 任何操作系统的最新版本                           |
| 1-11     | Apache Kafka                        | 任何操作系统的最新版本                           |
| 1-11     | Spring STS                          | 最新版本并配置使用 Java 12 JDK                  |
| 1-11     | Docker Engine                       | 任何操作系统的最新版本                           |
| 1-11     | Jaeger                              | 任何操作系统的最新版本                           |
| 1-11     | Keycloak                            | 与 Java 12 兼容的版本                           |
| 1-11     | OpenSSL                             | 任何操作系统的最新版本                           |
| 1-11     | Google Chrome                       |                                                  |
| 1-11     | Bootstrap 4.x                       |                                                  |


我们还提供了一个包含本书中使用的屏幕截图/图表彩色图像的 PDF 文件。[点击此处下载](https://packt.link/ohTNw)。


### 相关产品 <您可能喜欢的其他书籍>
* 使用 FastAPI 构建 Python Web API [[Packt]](https://www.packtpub.com/product/building-python-web-apis-with-fastapi/9781801076630?_ga=2.180798177.738679754.1661260461-1157268863.1584421665&utm_source=github&utm_medium=repository&utm_campaign=9781801076630) [[Amazon]](https://www.amazon.com/dp/1801076634)

* 使用 Sanic 进行 Python Web 开发 [[Packt]](https://www.packtpub.com/product/python-web-development-with-sanic/9781801814416?_ga=2.188147822.738679754.1661260461-1157268863.1584421665&utm_source=github&utm_medium=repository&utm_campaign=9781801814416) [[Amazon]](https://www.amazon.com/dp/1801814414)

## 了解作者
**Sherwin John Calleja Tragura**
是 Java、ASP .NET MVC 和 Python 应用程序方面的主题专家，在前端框架方面也有一定背景。他曾管理开发团队构建与制造业和固定资产、文档管理、记录管理、POS 和库存系统相关的各种应用程序。他在构建实验室信息管理系统（LIMS）和混合移动应用程序方面有咨询背景。自 2010 年以来，他还为 Python、Django、Flask、Jakarta EE、C#、ASP .NET MVC、JSF、Java 和一些前端框架课程提供企业训练营培训服务。他著有《Spring MVC Blueprints》和《Spring 5 Cookbook》等书籍，以及 Packt 视频《Modern Java Web Applications with Spring Boot 2.x》。


## 作者的其他书籍
* [Spring MVC Blueprints](https://www.packtpub.com/product/spring-mvc-blueprints/9781785888274?utm_source=github&utm_medium=repository&utm_campaign=9781785888274)
* [Spring 5.0 Cookbook](https://www.packtpub.com/product/spring-5-0-cookbook/9781787128316?utm_source=github&utm_medium=repository&utm_campaign=9781787128316)


### 下载免费 PDF

 <i>如果您已经购买了本书的印刷版或 Kindle 版本，您可以免费获得无 DRM 的 PDF 版本。<br>只需点击链接即可获取您的免费 PDF。</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781803245966">https://packt.link/free-ebook/9781803245966 </a> </p>