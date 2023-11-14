from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def statistics(self, request, pk=None):
        data = []

        for movie in Movie.objects.all():
            data.append({
                'id': movie.id,
                'title': movie.title,
                'average_rating': movie.get_average_rating(),
            })

        return Response(data)

    @action(detail=True, methods=['post'])
    def review(self, request, pk=None):
        serializer = MovieReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Review created.'}, status=201)

        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'])
    def todo(self, request, pk=None):
        data = {
            'detail': 'This endpoint is not implemented yet.',
        }

        return Response(data)
