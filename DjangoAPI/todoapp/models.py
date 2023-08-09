from django.db import models

# Create your models here.
class Todos(models.Model):
    todo = models.CharField("Todo", max_length=240)

    def __str__(self):
        return self.todo