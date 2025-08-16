from django.urls import path 
from .views import getBookList, getBookDetail

urlpatterns = [
    path('list/' , getBookList, name='book-list'),
    path('<str:pk>/', getBookDetail, name='book-detail'),
]