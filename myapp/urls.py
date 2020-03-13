from django.urls import path, include
from .views import *
 
urlpatterns = [
 
    path('likes/', LikeList.as_view() , name='like_list'), 
    path('likes/<int:pk>', LikeDetail.as_view(), name='like_detail'),
    path('posts/', PostList.as_view() , name='post_list'),   
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('comments/', CommentDetail.as_view(), name='comment_list'),
    path('comments/<int:pk>', CommentDetail.as_view() ,name='comment_detail'),
    path('user/create',UserCreate.as_view()),
]



# urlpatterns = [
 
#     path('likes/', like_list_post , name='like_list'), 
#     path('likes/<int:pk>', like_detail, name='like_detail'),
  
#     path('posts/', post_list_post , name='post_list'),   
#     path('posts/<int:pk>', post_detail, name='post_detail'),
#     path('comments/', comment_list_post, name='comment_list'),
#     path('comments/<int:pk>', comment_detail, name='comment_detail'),

#     path('user/create',user_create),
# ]