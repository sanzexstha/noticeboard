from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', post_list_post , name='post_list'),
    path('posts/<int:pk>', post_detail, name='post_detail'),
    path('user/create',user_create),
]