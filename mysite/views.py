
from django.shortcuts import render
from Book.models import Author,Book

def hello(request):
    return render(request, 'menu.html')

def book(request):
    authors=Author.objects.all()
    books= Book.objects.all()


    context = {'authors':authors,'books':books}
    return  render(request, 'book.html', context)


