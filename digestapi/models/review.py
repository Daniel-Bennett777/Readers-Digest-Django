from django.db import models
from django.contrib.auth.models import User  # Import the User model
from .models import Book  # Import the Book model

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        default=1,  # You can set a default value
        validators=[MinValueValidator(1), MaxValueValidator(10)]  # Set rating limits
    )
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)