from django.urls import path
from . import views

app_name = 'books'  # URL reverse 네이밍용

urlpatterns = [
    path('', views.index, name='index'),  # /books/
    path('create/', views.create, name='create'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/update/', views.update, name='update'),
    # path('<int:pk>/delete/', views.delete, name='delete'),

    # path('<int:book_pk>/threads/create/', views.thread_create, name='thread_create'),
    # path('threads/<int:pk>/', views.thread_detail, name='thread_detail'),
    # path('threads/<int:pk>/update/', views.thread_update, name='thread_update'),
    # path('threads/<int:pk>/delete/', views.thread_delete, name='thread_delete'),
]
