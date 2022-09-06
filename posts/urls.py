from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('details/<int:pk>', views.PostDetailAPI.as_view(), name='post_details'),
    path('list', views.PostListAPI.as_view(), name='post_list'),
]