from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    release_year = models.IntegerField()

    def get_average_rating(self):
        reviews = MovieReview.objects.filter(movie=self)
        return sum(review.rating for review in reviews) / len(reviews)

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class MovieReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.rating < 1 or self.rating > 5:
            raise ValueError('Rating must be between 1 and 5.')

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.movie.title} - {self.rating}'
