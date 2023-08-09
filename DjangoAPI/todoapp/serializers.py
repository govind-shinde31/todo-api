from rest_framework import serializers
from .models import Customer

class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos 
        fields = ['pk', 'todo',]
