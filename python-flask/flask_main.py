#!coding=utf8
"""
这是一个极简的 flask api示例
install:  pip install flask
run: python flask_main.py
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")    # URL目录
def hello():
    return "Hello Flask!"   # return string


if __name__ == "__main__":
    app.run()
    # 监听所有公网IP
    app.run(host='0.0.0.0')
