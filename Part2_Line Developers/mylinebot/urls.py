"""mylinebot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url

# 將 bot 的 urls 檔案 include 進來
# 此時 url 路徑為  /bot/callback/ ，就會運行 bot 底下的 callback 函數
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^bot/', include('bot.urls')),
]


