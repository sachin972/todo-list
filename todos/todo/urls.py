from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('<int:todo_id>', views.todoList, name = 'todo'),
    path('update/<int:todo_id>', views.update, name = 'update'),
    path('add', views.add, name = "add"),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('update/updaterecord/<int:todo_id>',views.updaterecord, name = 'updaterecord')
]