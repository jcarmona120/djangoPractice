from django.urls import path, re_path
from django.conf.urls import url
from first_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('whatawebsite', views.whatawebsite)
]
