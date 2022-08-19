# fastapi-manager

FastApi项目简单初始化.

## 安装

> pip install fastapi-manager

## 如何使用

完整示例请看 [fastapi-manger的使用示例](https://gitee.com/cheerxiong/fastapi-demo)

### 如何初始化

```python
from fastapi import FastAPI
from fastapi_manager import manager

app = FastAPI()

manager(app, 'conf.setting')
```

**conf.setting**这个配置为importlib包可以动态导入的字符串，也可以是一个确定的对象；**manager**方法会获取配置对象中的**
Router**、**MiddleWare**、**Extend**三个参数去动态导入接口路由、中间件、第三方扩展，其中**Extend**
中的扩展必须按照固定格式编写；因为**manager**初始化的执行的时候会把配置暂时存放到**fastapi.state**
中，所以可以在配置文件中配置扩展所需要的配置。这里有定义好的[扩展](https://gitee.com/cheerxiong/fastapi-manager/tree/master/fastapi_manager/extend)
，可以根据这个编写自己的扩展。

### 全局配置

```python
from fastapi_manager.manager import static_setting
```

因为**fastapi**没有实现全局的配置，仅有一个类似的对象可以**fastapi.state**存放全局配置，但是不推荐，**fastapi-manager**
也仅仅只是暂时使用一下之后便删除了**state**中的配置，所以这里实现了一个可以供全局调用的配置。

### 第三方扩展

#### 日志扩展

```python
# setting.py

Extend = [
    'fastapi_manager.extend.logger_extend'
]

# 日志过滤
IgnoreLogger: list
# 日志级别
LogLevel: int
# 日志格式
LogFormatter: str
```

只需要配置对象中填写即可，仅仅提供简单的日志定义**IgnoreLogger**、**LogLevel**以及**LogFormatter**是可以自己控制的参数。

#### 异步orm框架tortoise-orm扩展

```python
# setting.py

Extend = [
    'fastapi_manager.extend.orm_extend'
]

# 数据库配置
Database: dict
```

在**Extend**配置完成之后，必须配置**Database**
配置，详情可以参考 [tortoise-orm](https://tortoise-orm.readthedocs.io/en/latest/examples/fastapi.html)

#### 异步redis框架tortoise-orm扩展

```python
# setting.py

Extend = [
    'fastapi_manager.extend.cache_extend'
]

# 缓存配置
Cache: dict
```

在**Extend**配置完成之后，必须配置**Cache**
配置，详情可以参考 [aioredis](https://aioredis.readthedocs.io/en/latest/getting-started/)