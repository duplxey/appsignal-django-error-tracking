from django.core.management.base import BaseCommand

from movies.models import Movie, MovieReview


class Command(BaseCommand):
    help = 'Populates the database with a few movies and reviews.'

    def handle(self, *args, **options):
        american_psycho = Movie.objects.create(
            title='American Psycho',
            description='A dark comedy-drama that follows the life of Patrick Bateman.',
            release_year=2000,
        )
        MovieReview.objects.create(movie=american_psycho, rating=5)
        MovieReview.objects.create(movie=american_psycho, rating=4)
        MovieReview.objects.create(movie=american_psycho, rating=5)

        fight_club = Movie.objects.create(
            title='Fight Club',
            description='A drama that tells the story of an insomniac office worker.',
            release_year=1999
        )
        MovieReview.objects.create(movie=fight_club, rating=4)
        MovieReview.objects.create(movie=fight_club, rating=5)
        MovieReview.objects.create(movie=fight_club, rating=3)

        a_clockwork_orange = Movie.objects.create(
            title='A Clockwork Orange',
            description='A dystopian crime film based on the novel by Anthony Burgess.',
            release_year=1971
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
