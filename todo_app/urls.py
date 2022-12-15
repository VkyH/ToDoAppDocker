from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('todolist/',views.todolist,name='todolist'),
    path('delete/<str:pk>',views.delete_task,name='delete_task'),
    path('edit/<str:pk>',views.edit_task,name='edit_task'),
    path('complete/<str:pk>',views.completed_status,name='completed_status'),
    path('pending/<str:pk>',views.pending_status,name='pending_status'),
    path('contact/',views.contact,name='contact'),
    path('aboutus/',views.aboutus,name='aboutus'),
   
    
]
