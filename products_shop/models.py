from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Products(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='products_shop',verbose_name='автор',blank=True)
    title=models.CharField(max_length=100,verbose_name='название')
    image=models.ImageField(upload_to='posts_img/',blank=True,verbose_name='фото')
    description=models.TextField(blank=True,verbose_name='описание')
    created_at=models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # size=models.DecimalField(max_digits=90)




    def __str__(self) -> str:
        return self.title 
