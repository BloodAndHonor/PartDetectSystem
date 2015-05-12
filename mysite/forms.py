# -*- coding: utf-8 -*-
from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


class RegForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
