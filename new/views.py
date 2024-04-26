from django.shortcuts import render
from .models import Book,Genre


# Create your views here.


def index(request):
    
    books=Book.objects.filter(status='out of stock').order_by('author')
   

    return render(request,'main/index.html',{'books':books})


def index(request):
    genres=Genre.objects.all()
    return render(request,'new/index.html',{'genres':genres})

def book_list(request,slug):
    books=Book.objects.filter(genre__slug=slug)
    return render(request,'new/book_list.html',{'books':books})

def author(request,pk):
    author=Authors.objects.get(pk=pk)
    author_books=author.books.all()
    return render(request,'new/author.html',{'author':author,'books':author_books})
