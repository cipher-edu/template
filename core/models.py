from django.db import models
from django.urls import reverse

# Create your models here.
class LandingHead(models.Model):
    logos = models.ImageField(upload_to='logo/')
    landing_image = models.ImageField(upload_to='images/')
    landing_title = models.TextField(max_length=250)

#cattegory

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'categoriya'
        verbose_name_plural = 'categoriyalarni kiriting'
    
    def __str__(self):
        return self.name

#add post

class Postl(models.Model):
    post_image = models.ImageField(upload_to='posts/')
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    post_date = models.DateField()
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name  = 'Post'
        verbose_name_plural = 'Posts left'
    def __str__(self):
        return self.post_title
class Postr(models.Model):
    post_image = models.ImageField(upload_to='posts/')
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    post_date = models.DateField()
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name  = 'Post'
        verbose_name_plural = 'Posts right'
    def __str__(self):
        return self.post_title

class Postarchive(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    archive_image = models.ImageField(upload_to='posts')
    archive_title = models.CharField(max_length=150)
    archive_content = models.TextField()
    archive_date = models.DateField()
    archive_author = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'archive'
        verbose_name_plural = 'archive post yaratish'

    def  __str__(self):
        return self.archive_title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})