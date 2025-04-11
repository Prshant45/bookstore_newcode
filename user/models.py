from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    """
    Custom user model extending AbstractUser.
    """
    # Add any additional fields you want to include in your user model
    # For example:
    # bio = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
        db_table = 'users'

class Books(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']
        db_table = 'books'
# Create your models here.
