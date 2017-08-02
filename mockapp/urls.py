from django.conf.urls import url
from django.contrib import admin
import  views


urlpatterns = [
    url(r'^api', views.api),
    url(r'^getReq', views.getReq),

]
