# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
#首先导入HttpResponse模块
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    """
    :param request: 这个参数必须有，类似self的默认规则，可以改，它封装了用户请求的所有内容
    :return: 不能直接返回字符串，必须有HttpResponse这个类封装起来，这是Django的规则
    """
    return HttpResponse("Hello Django!")
