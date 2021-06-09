

## intro
swagger ui的实现方式
* flasgger:  `pip install flasgger`
* restplus:  `pip install flask_restplus`

## flasgger
flasgger配置文件解析：
  在flasgger的配置文件中，以yaml的格式描述了flasgger页面的内容；
  * tags标签中可以放置对这个api的描述和说明；
  * parameters标签中可以放置这个api所需的参数，如果是GET方法，可以放置url中附带的请求参数，如果是POST方法，可以将参数放置在schema子标签下面；
  * responses标签中可以放置返回的信息，以状态码的形式分别列出，每个状态码下可以用schema标签放置返回实体的格式；

flasgger的不足
  flasgger的配置文件中，对于POST方法，在描述POST body的schema标签中，不支持以yaml格式描述的数组或嵌套的object，这使得页面上面无法显示这类POST body的example；
  解决方案：将这类POST body的example放置在description部分（三横杠”—“上面的部分），由于description部分是用html格式解析的，所以可以以html的语法编写；


## restplus

依赖：flask==1.1.2 flask_restplus==0.3.9 werkzeug==0.16.1
