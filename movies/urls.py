from django.urls import include, path
from rest_framework import routers

from movies.views import MovieViewSet, MovieStatisticsView, MovieReviewView

router = routers.DefaultRouter()
router.register(r'', MovieViewSet)

urlpatterns = [
    path('statistics/', MovieStatisticsView.as_view()),
    path('review/', MovieReviewView.as_view()),
    path('', include(router.urls)),
]
