import django
from django.test import TestCase
from django.urls import reverse
from reviews.models import Reviews, Shows_Movies
import pytest

# Create your tests here.


def test_index_access_reviews():
    url = reverse('reviews_index')
    assert url == "/reviews/"

@pytest.mark.django_db
def test_create_show_movie():
    show_movie = Shows_Movies.objects.create(
        title= "Fantasia",
        type= "MOVIE",
        description= "Walt Disney's timeless masterpiece is an extravaganza of sight and sound! See the music come to life, hear the pictures burst into song and experience the excitement that is Fantasia over and over again.",
        release_year= "1940-11-13",
        age_certification= "G",
        runtime= 120,
        genre= "['animation', 'family', 'music', 'fantasy']",
        seasons= 0
    )
    assert show_movie.title == "Fantasia"
