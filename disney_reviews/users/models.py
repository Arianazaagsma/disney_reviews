# models for tables

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=280)