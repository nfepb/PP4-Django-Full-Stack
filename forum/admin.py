from django.contrib import admin
from .models import Movie, Review, WatchlistItem, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):

    list_display = (
        'movie_title', 'movie_genre', 'year_released', 'movie_created_on'
        )
    search_fields = ('movie_title', 'directors')
    list_filter = ('movie_updated_on', 'movie_genre')
    summernote_fields = ('content')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = (
        'reviewed_movie', 'author', 'review_rating', 'review_created_on'
        )
    search_fields = ('author', 'content')
    list_filter = ('review_rating', 'reviewed_movie')


@admin.register(WatchlistItem)
class WatchlistItemAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
