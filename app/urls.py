from django.urls import path
from .views import *

urlpatterns =[
    path('get-todo/', get_todo, name='get_todo'),
    path('put-todo/', put_todo, name='put_todo'),
    path('patch-todo/', patch_todo, name='patch_todo'),
    path('delete-todo/', delete_todo, name='delete_todo'),
    path('register/', RegisterUser.as_view(), name='register_user')
]