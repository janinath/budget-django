from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name=models.TextField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=200,blank=True)
    cat_image=models.ImageField(upload_to='photos/categories',blank=True)
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('store:products_by_category',args=[self.slug])
    def __str__(self):
        return self.category_name
    