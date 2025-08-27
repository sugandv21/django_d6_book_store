from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Category

def home(request):
    books = Book.objects.all()
    return render(request, 'store/index.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'store/authors.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/books.html', {'books': books})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

def author_books(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    return render(request, 'store/author_books.html', {'author': author, 'books': books})

def category_books(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = category.books.all()
    return render(request, 'store/category_books.html', {'category': category, 'books': books})
