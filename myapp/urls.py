from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('posts/', views.post_list_post),
    path('posts/<int:pk>', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
