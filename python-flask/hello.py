#!coding=utf8

from flask import Flask
app = Flask(__name__)

@app.route("/")    # URL目录
def hello():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run()
    # 监听所有公网IP
    app.run(host='0.0.0.0')
