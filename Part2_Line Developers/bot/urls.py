# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:14:59 2022

@author: hmkao
"""

from django.conf.urls import include, url
from . import views


# 用來串接callback主程式
urlpatterns= [
        url('^callback/', views.callback),
        ]

