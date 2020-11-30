from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("process", views.process),
    path("books/<int:book_id>",views.books),
    path("add_author", views.add_author),
    path("authors", views.authors),
    path("process_two", views.process_two),
    path("authors/<int:author_id>", views.add_book),
    path("send_it", views.send_it),
    
