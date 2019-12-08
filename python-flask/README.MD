
## plugins
```sh
$ pip freeze
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-1.0.2 itsdangerous-0.24
```

## install
```sh
$ pip install Flask
```

## 启动
```sh
# 单进程启动
$ python hello.py
# gunicorn启动
$ gunicorn -w 2 hello:app
```
访问地址：http://127.0.0.1:5000
