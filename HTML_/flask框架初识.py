#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: flask框架初识.py
@date: 2020/7/16
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/index/', methods=['GET', 'POST'])
def index():
    print(request.form) # 获取form表单提交过来的非文件数据
    print(request.files)  # 获取文件数据
    file_obj = request.files.get('myfile')
    file_obj.save(file_obj.name)
    return 'ok'


app.run()
