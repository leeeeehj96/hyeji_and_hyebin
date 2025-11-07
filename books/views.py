from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from .models import Book, Thread
from .forms import BookForm, ThreadForm

@require_http_methods(['GET'])
def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context)


def thread_create (request, book_pk):
    book = Book.objects.get(pk=book_pk)
    thread = ThreadForm()
    context = {
        'book' : book,
        'thread' : thread,
    }
    return render(request, 'detail', context, book_pk)