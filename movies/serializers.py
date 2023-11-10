from rest_framework import serializers

from movies.models import Movie, MovieReview


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class InlineMovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ['id', 'rating', 'created_at', 'updated_at']
