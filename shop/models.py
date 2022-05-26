from statistics import mode
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Shop(models.Model):

    product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2,default="0.00")
    overview = models.TextField(max_length=200,default="N/A")
    material = models.TextField(max_length=200, default="N/A")
   
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='shop')
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='images/')
    posted = models.DateField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.product