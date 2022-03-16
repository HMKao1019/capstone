# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:14:59 2022

@author: hmkao
"""

from django.conf.urls import include, url
from . import views

urlpatterns= [
        url('^callback/', views.callback),
        ]

