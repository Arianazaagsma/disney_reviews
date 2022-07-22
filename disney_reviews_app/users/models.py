# models for tables

from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from reviews.models import Reviews


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=280)


class Users_Reviews(models.Model):
    user_id = models.ForeignKey(Users, on_delete=CASCADE)
    review_id = models.ForeignKey(Reviews, on_delete=CASCADE)