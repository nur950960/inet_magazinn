from django.db import models
from django.contrib.auth import get_user_model
from products_shop.models import Products

User=get_user_model()

class Like(models.Model):
    user=models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    post=models.ForeignKey(Products,related_name='likes',on_delete=models.CASCADE)


class Comment(models.Model):
    user=models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    post=models.ForeignKey(Products,related_name='cooments',on_delete=models.CASCADE)
    body=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True) 


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    rating = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)
