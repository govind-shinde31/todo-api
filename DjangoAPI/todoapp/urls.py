from django.urls import include, path
from .views import TodoCreate, TodosList


urlpatterns = [
    path('todo/', TodoCreate.as_view(), name='create-todo'),
    path('', TodosList.as_view()),
]