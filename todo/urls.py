from django.urls import path
from todo import views


urlpatterns = [
    path('createtodo', views.createtodo, name='createtodo'),
    path('alltodo', views.alltodo, name='alltodo'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletetodo'),
    path('tododetail/<int:id>', views.tododetail, name='tododetail'),
    path('todoedit/<int:id>', views.todoedit, name='todoedit'),
]