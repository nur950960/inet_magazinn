from django.db import models

from new.models import Book

# Create your models here.


class Order(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='orders')
    phone=models.CharField(max_length=13)
    address=models.TextField()
    city=models.CharField(max_length=100)
    email=models.EmailField()


    def __str__(self):
        return f'{self.email}-{self.phone}'


# Create your models here.


