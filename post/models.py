from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='poats',verbose_name='Автор',blank=True)
    title=models.CharField(max_length=100,verbose_name='название')
    image=models.ImageField(upload_to='posts_img/',blank=True,verbose_name='фото')
    description=models.TextField(blank=True,verbose_name='описание')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    
