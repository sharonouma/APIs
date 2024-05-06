from .models import Book
from rest_framework import serializers


class BookSerialier(serializers.ModelSerializer):
    class meta:
        model = Book
        fields = '__all__'
        
        
        