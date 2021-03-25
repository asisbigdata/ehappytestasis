"""linebotTest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from test2api import views
from test2api.views import sayhello, hello3,hello4,hello5

urlpatterns = [
    url('^callback', views.callback),
    path('admin/', admin.site.urls),
    url(r'^$', sayhello), 
    url(r'^hello3/(\w+)/$', hello3), 
    url(r'^hello4/(\w+)/$', hello4),
    url(r'^hello5/(\w+)/$', hello5),
    path('sayhello/', sayhello),
    path('hello5/', hello5),
    path(r'^hello4/(\w+)/$', hello4),
]
