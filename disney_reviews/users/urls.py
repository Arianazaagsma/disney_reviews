from django.urls import path
from users import views as users_views

urlpatterns = [
    path('', users_views.index, name='users_index'), 
    path('api/users/add_user', users_views.add_user)
]