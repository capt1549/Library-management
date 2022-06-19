from rest_framework import serializers
# from rest_framework import Books
from .models import Books

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model= Books
        fields= '__all__'