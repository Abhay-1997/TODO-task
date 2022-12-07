from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/', views.add, name='add'),
    path('alltasks/', views.all, name='all'),
    path('completetask/', views.complete, name='complete'),
    path('pendingtask/', views.pending, name='pending'),
    path('updatetask/<int:pk>', views.update, name='update'),
    path('deletetask/<int:pk>', views.delete, name='delete'),

]
