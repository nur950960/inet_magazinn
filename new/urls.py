from django.urls import path
from .views import index,book_list,author
urlpatterns=[
    path('',index,name='home'),
    path('<str:slug>/',book_list,name='book-list'),
    path('author/<int:pk>/',author,name='author')
]