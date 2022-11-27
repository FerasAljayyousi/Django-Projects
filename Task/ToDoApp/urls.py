from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_todo_items, name = 'list_todo_items'),
    path('insert', views.insert, name = 'insert'),
    path('delete/<int:to_id>/', views.delete, name = 'delete')
]


