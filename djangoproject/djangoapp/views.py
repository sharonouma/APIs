from django.shortcuts import render
from  .models import Book
from .serializers import BookSerializer
from rest_framework import generics


# Create your views here.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
