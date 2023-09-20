from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Create your models here.
class Catergory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(upload_to='category')

    class Meta:
        ordering = ('name',) 
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    catergory = models.ForeignKey(Catergory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('marketplace:item_detail', args=[self.id])