from rest_framework import serializers
from reviews.models import Reviews, Shows_Movies, Users_Reviews


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'rating', 'review', 'show_movie_id')

class ShowsMoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shows_Movies
        fields = ('id', 'title', 'type', 'description', 'release_year', 'age_certification', 'runtime', 'genre', 'seasons')

class UsersReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users_Reviews
        fields = ('user_id', 'review_id')