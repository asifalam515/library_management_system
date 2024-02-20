
from django.urls import path,include
from .views import book_list,review_book
urlpatterns = [
  
    path('books/', book_list,name='books'),
    path('review_book/<int:borrowed_book_id>/', review_book, name='review_book'),

]
