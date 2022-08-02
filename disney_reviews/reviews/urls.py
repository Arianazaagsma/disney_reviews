from django.urls import path
from reviews import views as reviews_views

urlpatterns = [
    path('', reviews_views.index, name='reviews_index'),
    path('reviews/', reviews_views.reviews_list, name='reviews_list'),
    path('<int:pk>/delete_review/', reviews_views.delete_review, name='delete_review'), 
    path('add_show_movie/', reviews_views.add_show_movie, name='add_show_movie'), 
    path('<int:pk>/edit_review/', reviews_views.edit_review, name='edit_review')
    ]