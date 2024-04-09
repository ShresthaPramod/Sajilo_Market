from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=202)

    class Meta:
        ordering = ('name',)
        # verbose_name_plural = 'Category'
    
    def __str__(self):
        return self.name
    


class Item(models.Model):
    name = models.CharField(max_length=202)
    description = models.TextField( blank=True )
    price =models.FloatField()
    category = models.ForeignKey(Category, related_name='items',  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    

    
    def __str__(self):
        return self.name
    

    

