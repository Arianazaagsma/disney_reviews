import django
from django.test import TestCase
from django.urls import reverse
from reviews.models import Reviews
import pytest

# Create your tests here.


def test_index_access_reviews():
    url = reverse('reviews_index')
    assert url == "/reviews/"
