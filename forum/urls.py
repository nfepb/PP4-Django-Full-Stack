from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>', views.MovieDetails.as_view(), name='movie_detail'),
    path(
        'genre/<slug:slug>', views.GenreDetail.as_view(), name='genre_detail'
        ),
]
