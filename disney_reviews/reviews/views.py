from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews.models import Reviews, Shows_Movies, Users_Reviews
from reviews.serializers import ReviewsSerializers, ShowsMoviesSerializers, UsersReviewsSerializers
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You are at the reviews index.")

class reviews_list(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'reviews/reviews_list.html'

    def get(self, request):
        queryset = Reviews.objects.all()
        return Response({'reviews': queryset})

@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
    
        reviews_serializer = ReviewsSerializers(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)
    
    elif request.method == 'POST':
        reviews_data = JSONParser().parse(request)
        reviews_serializer = ReviewsSerializers(data=reviews_data)
        if reviews_serializer.is_valid():
            reviews_serializer.save()
            return JsonResponse(reviews_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(reviews_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_review(request, pk):
    try: 
        review = Reviews.objects.get(pk=pk)
    except Reviews.DoesNotExist:
        return JsonResponse({'message': 'The review does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    review.delete()
    return JsonResponse({'message': 'The review was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_show_movie(request):
    shows_movies_data = JSONParser().parse(request)
    shows_movies_serializer = ShowsMoviesSerializers(data=shows_movies_data)
    if shows_movies_serializer.is_valid():
        shows_movies_serializer.save()
        return JsonResponse(shows_movies_serializer.data,
                            status=status.HTTP_201_CREATED)
    return JsonResponse(shows_movies_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_review(request, pk):
    try: 
        review = Reviews.objects.get(pk=pk)
    except Reviews.DoesNotExist:
        return JsonResponse({'message': 'The review does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    review_data = JSONParser().parse(request)
    review_serializer = ReviewsSerializers(review, data=review_data)
    if review_serializer.is_valid():
        review_serializer.save()
        return JsonResponse(review_serializer.data,
                            status=status.HTTP_201_CREATED)
    return JsonResponse(review_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)