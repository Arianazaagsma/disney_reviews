# models for tables

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Users

class Shows_Movies(models.Model):
    title = models.CharField(max_length=280)
    type = models.CharField(max_length=6)
    description = models.CharField(max_length=500)
    release_year = models.DateField()
    age_certification = models.CharField(max_length=6)
    runtime = models.IntegerField()
    genre = models.CharField(max_length=20)
    seasons = models.IntegerField


class Reviews(models.Model):
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    review = models.CharField(max_length=280)
    show_movie_id = models.ForeignKey(Shows_Movies, on_delete=models.CASCADE)

class Users_Reviews(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    review_id = models.ForeignKey(Reviews, on_delete=models.CASCADE)
