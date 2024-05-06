from django.urls import path
from .views import BookListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name= 'book_list_create')
]

