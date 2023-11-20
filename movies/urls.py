from django.urls import path

from movies import views

urlpatterns = [
    path('statistics/', views.statistics_view, name='movies-statistics'),
    path('review/', views.review_view, name='movies-review'),
    path('', views.index_view, name='movies-index'),
]
