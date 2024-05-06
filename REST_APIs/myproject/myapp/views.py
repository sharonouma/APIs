from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer

# Create your views here.

def book_list (request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many= True)
        return JsonResponse (serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse (serializer.data, status = 201)
    return JsonResponse (serializer.errors, status = 400)

def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not Found'}, status = 404)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid ():
         serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status = 400) 

    