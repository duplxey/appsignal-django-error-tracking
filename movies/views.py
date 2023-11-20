from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from movies.models import Movie, MovieReview


def index_view(request):
    queryset = Movie.objects.all()
    data = [movie.serialize_to_json() for movie in queryset]

    return JsonResponse(data, safe=False)


def statistics_view(request):
    queryset = Movie.objects.all()
    data = []

    for movie in queryset:
        data.append({
            'id': movie.id,
            'title': movie.title,
            'average_rating': movie.get_average_rating(),
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def review_view(request):
    movie_id = request.POST.get('movie')
    rating = request.POST.get('rating')

    if (movie_id is None or rating is None) or (not movie_id.isdigit() or not rating.isdigit()):
        return JsonResponse({
            'detail': 'Please provide a `movie` (int) and `rating` (int).',
        }, status=400)

    movie_id = int(movie_id)
    rating = int(rating)

    if rating < 1 or rating > 5:
        return JsonResponse({
            'detail': 'Rating must be between 1 and 5.',
        }, status=400)

    try:
        movie = Movie.objects.get(id=movie_id)
        MovieReview.objects.create(
            movie=movie,
            rating=rating,
        )

        return JsonResponse({
            'detail': 'A review has been successfully posted',
        })

    except Movie.DoesNotExist:
        return JsonResponse({
            'detail': 'Movie does not exist.',
        }, status=400)
