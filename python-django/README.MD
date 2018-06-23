
## install
```
$ pip install  django          #安装最新版本的Django
```

## startproject
命令行创建项目
> $ django-admin.py startproject mysite
```
Django将自动生成下面的目录结构：
mysite/
├── manage.py           # Django管理主程序
├── mysite
│   ├── __init__.py
│   ├── settings.py     # 主配置文件
│   ├── urls.py         # URL路由系统文件
│   └── wsgi.py         # 网络通信接口
└── template            # 该目录放置HTML文件模板
```

## startapp 创建APP
在每个Django项目中可以包含多个APP，相当于一个大型项目中的分系统、子模块、功能部件等等，相互之间比较独立，但也有联系，所有的APP共享项目资源。
>$ python manage.py startapp cmdb
```
cmdb/
├── admin.py      
├── apps.py       
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py    
├── tests.py
└── views.py
```

## 编写路由规则 urls.py
路由都在urls文件里，它将浏览器的URL映射到响应的业务处理逻辑。
```
# urls.py
from django.conf.urls import url
from django.contrib import admin
from cmdb import views
 
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
]
```

## 编写业务处理逻辑 views.py
```
# views.py
from django.shortcuts import render
#首先导入HttpResponse模块
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    """
    :param request: 这个参数必须有，类似self的默认规则，可以改，它封装了用户请求的所有内容
    :return: 不能直接返回字符串，必须有HttpResponse这个类封装起来，这是Django的规则
    """
    return HttpResponse("Hello,World")
```

## run
运行Web服务
> $ python manage.py runserver 8080
