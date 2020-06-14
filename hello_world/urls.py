from django.urls import path
from hello_world.views import index, actors1, actors2, comments, create, detail

urlpatterns = [
    path('', index),
    path('actors1/', actors1),
    path('actors2/', actors2),
    path('comments/', comments),
    path('create/', create),
    path('posts/<int:post_id>', detail)
]
