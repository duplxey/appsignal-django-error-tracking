from django.contrib import admin

from movies.models import Movie, MovieReview

admin.site.register(Movie)
admin.site.register(MovieReview)
