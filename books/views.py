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

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('books:detail', book.pk)
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'books/create.html', context)

@require_http_methods(['GET'])
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    threads = book.threads.all().order_by('-created_at')
    context = {
        'book': book,
        'threads': threads,
    }
    return render(request, 'books/detail.html', context)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:detail', book.pk)
    else:
        form = BookForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/update.html', context)

@require_POST
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # (선택) 로그인 사용 시 작성자 체크 로직 추가 가능
    book.delete()
    return redirect('books:index')

@require_http_methods(['GET', 'POST'])
def thread_create(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.book = book
            thread.save()
            return redirect('books:thread_detail', thread.pk)
    else:
        form = ThreadForm()
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/thread_create.html', context)

@require_http_methods(['GET'])
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    context = {
        'thread': thread,
    }
    return render(request, 'books/thread_detail.html', context)

@require_http_methods(['GET', 'POST'])
def thread_update(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('books:thread_detail', thread.pk)
    else:
        form = ThreadForm(instance=thread)
    context = {
        'form': form,
        'thread': thread,
    }
    return render(request, 'books/thread_update.html', context)

@require_POST
def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    book_pk = thread.book.pk
    thread.delete()
    return redirect('books:detail', book_pk)
