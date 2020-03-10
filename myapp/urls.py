from django.urls import path, include
from .views import *


# from rest_framework import routers
 

# router = routers.DefaultRouter()
# router.register('posts', PostModelViewSet)
# router.register('comments', CommentViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    path('posts/', post_list_post , name='post_list'),   
    path('posts/<int:pk>', post_detail, name='post_detail'),
    path('comments/', comment_list_post, name='comment_list_post'),
    # path('comments/<int:pk>', comment_detail, name='comment_detail'),

    path('user/create',user_create),
]