import django
from django.test import TestCase
from django.urls import reverse
from users.models import Users
import pytest

# Create your tests here.


def test_index_access_users():
    url = reverse('users_index')
    assert url == "/users/"