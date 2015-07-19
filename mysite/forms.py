# -*- coding: utf-8 -*-
from django import forms

#上传文件的表单格式
class DocumentForm(forms.Form):

    docfile = forms.FileField(
        label='Select a file',        
    )

#用户注册的表单格式
class RegForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
#用户登录的表单格式
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
