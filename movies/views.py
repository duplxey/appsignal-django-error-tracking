from rest_framework import viewsets, views
from rest_framework.response import Response

from movies.models import Movie, MovieReview
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatisticsView(views.APIView):

    def get(self, request, format=None):
        data = {}

        for movie in Movie.objects.all():
            data[(movie.id, movie.title)] = movie.get_average_rating()

        return Response(data)


class MovieReviewView(views.APIView):

    def post(self, request, format=None):
        movie_id = request.data.get('movie', None)
        rating = request.data.get('rating', None)

        if movie_id is None or rating is None:
            return Response({'detail': 'Please provide a movie and a rating.'}, status=400)

        try:
            MovieReview.objects.create(
                movie=Movie.objects.get(id=movie_id),
                rating=request.data.get('rating'),
            )
            return Response({'success': 'Review created.'}, status=201)
        except Movie.DoesNotExist:
            return Response({'detail': 'Movie not found.'}, status=404)
