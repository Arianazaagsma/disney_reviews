from django.urls import path
from reviews import views as reviews_views

urlpatterns = [
    path('', reviews_views.index, name='index'),
    path('api/reviews/', reviews_views.reviews_list),
    path('api/reviews/<int:pk>/', reviews_views.delete_review), 
    path('api/reviews/add_movie', reviews_views.add_show_movie)]