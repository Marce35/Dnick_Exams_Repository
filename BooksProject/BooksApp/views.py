from django.shortcuts import render, redirect

from BooksApp.forms import BookForm
from BooksApp.models import Book


# Create your views here.

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {'books': books})


def edit_book(request, id):
    book_instance = Book.objects.filter(id=id).get()
    if request.method == 'POST':
        book = BookForm(request.POST, instance=book_instance)
        if book.is_valid():
            book.save()
        return redirect("/books")
    else:
        book = BookForm(instance=book_instance)
        return render(request, "edit_book_form.html", {'form': book})
