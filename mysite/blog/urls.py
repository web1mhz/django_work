from django.urls import path, re_path
from . import views


app_name ="blog"

urlpatterns=[
    #path('', views.post_list, name='post_list'),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]