#coding:utf8
"""
flasgger实现swagger ui
@requirement: flasgger
@run: python flasgger_main.py
 http://localhost:5000/apidocs/
"""

import sys
import random

from flask import Flask,Blueprint,render_template,request,redirect,jsonify
from flasgger import Swagger,swag_from

app = Flask(__name__)
Swagger(app)

@app.route('/api/<string:language>/', methods=['GET'])
@swag_from('index.yaml')  #可以从外部导入yaml文件，作为swagger api描述
def index(language):
    """
    This is the language awesomeness API
    Call this api passing a language name and get back its features
    """
    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic", 
        "simple", "powerful", "amazing", 
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


if __name__ == '__main__':
    # run here
    app.run(debug=True)