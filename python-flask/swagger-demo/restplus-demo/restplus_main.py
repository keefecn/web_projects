#coding:utf8
"""
restplus 实现swagger ui
@refer: Building beautiful REST APIs using Flask, Swagger UI and Flask-RESTPlus https://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
@requirement: flask==1.1.2 flask_restplus==0.3.9 werkzeug==0.16.1
@run: python restplus_main.py
@TODO: werkzeug新版本引发导入错误
"""

from flask import Flask
from flask_restplus import Api, Resource, fields
#from werkzeug.utils import cached_property

app = Flask(__name__)
api = Api(app)

a_language = api.model('language', {
    'language': fields.String('TheLanguage'),
    'id': fields.Integer('ID')
})

languages = list()
python = {'language': 'python', 'id': 1}
languages.append(python)

@api.route('/language')
class Language(Resource):
    @api.marshal_with(a_language, envelope='data') # envelope在这里
    def get(self):
        return languages

    @api.expect(a_language) # API文档定义
    def post(self):
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result': 'Language added'}, 201


if __name__ == '__main__':
    app.run(debug=True)
