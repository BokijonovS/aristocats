from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

class Gender(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

class Cat(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    age = models.IntegerField(verbose_name='Age', null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, verbose_name='Color')
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, verbose_name='Gender')
    photo = models.ImageField(upload_to='images/', verbose_name='Image', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    views = models.IntegerField(default=0, verbose_name='Views', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'
        ordering = ['-pk']

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    photo = models.ImageField(upload_to='users/', null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name='Phone number', null=True, blank=True)
    mobile = models.CharField(max_length=13, verbose_name='Mobile', null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name='Email')
    site = models.URLField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    job2 = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = 'Custom user'
        verbose_name_plural = 'Custom users'
        ordering = ['-pk']



class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Cat, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment owner: {self.commentator.username}\nComment: {self.text}'

    class Meta:
        ordering = ['-pk']



