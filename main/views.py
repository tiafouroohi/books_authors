from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    all_book = Book.objects.all()
    all_author = Author.objects.all()
    context = {
        "all_book" : all_book,
        "all_author" : all_author,
    }
    return render(request, "index.html", context)

def process(request):
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        
    )
    return redirect("/")

def books(request, book_id):
    this_book = Book.objects.get(id=book_id)
    context = {
        'book': this_book,
        'all_author': Author.objects.all()
    }
    return render(request, "book.html", context)

def add_author(request):
    print(request.POST)
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author_id'])
    print(f'This is my book: {book.title} and this is my author: {author.first_name}')
    
    book.authors.add(author)
    return redirect(f'/books/{book.id}')

def authors(request):
    all_book = Book.objects.all()
    all_author = Author.objects.all()
    context = {
        "all_book" : all_book,
        "all_author" : all_author,
    }
    return render(request,"index2.html", context)

def process_two(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        
    )
    return redirect("/authors")

def add_book(request, author_id):
    this_author = Author.objects.get(id=author_id)
    context = {
        'author': this_author,
        'all_book': Book.objects.all()
    }
    return render(request, "author.html", context)

def send_it(request):
    print(request.POST)
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=request.POST['author_id'])
    author.books.add(book)
    return redirect(f'/authors/{author.id}')


