from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.author_list, name='authors'),
    path('books/', views.book_list, name='books'),
    path('categories/', views.category_list, name='categories'),
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
    path('category/<int:category_id>/books/', views.category_books, name='category_books'),
]
