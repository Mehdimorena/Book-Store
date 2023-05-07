from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)


    def __str__(self):
        return self.title   # injuri ham mishe nevesh return f'Pself.author}: {self.title}
