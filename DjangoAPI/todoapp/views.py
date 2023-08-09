from django.shortcuts import render

# Create your views here.
from .models import Todos
from rest_framework import generics
from .serializers import TodosSerializer


class TodoCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Todos.objects.all(),
    serializer_class = TodosSerializer

class TodosList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer