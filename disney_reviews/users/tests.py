import django
from django.test import TestCase
from django.urls import reverse
from users.models import Users
import pytest

# Create your tests here.


def test_index_access_users():
    url = reverse('users_index')
    assert url == "/users/"


@pytest.mark.django_db
def test_create_user():
    user = Users.objects.create(
        username='test_username',
        password='test_password'
    )
    assert user.username == "test_username"


@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True