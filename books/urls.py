
from django.urls import path,include
from .views import book_list
urlpatterns = [
  
    path('books/', book_list,name='books'),
]
