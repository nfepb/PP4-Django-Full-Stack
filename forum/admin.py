from django.contrib import admin
from .models import Movie, Review, WatchlistItem, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    # Defines the fields visible in Admin panel for the Movie model

    list_display = (
        'movie_title', 'movie_genre', 'year_released', 'movie_created_on'
        )
    # From Django Slug Tutorial:
    prepopulated_fields = {'slug': ('movie_title', 'director')}
    search_fields = ('movie_title', 'director')
    list_filter = ('movie_updated_on', 'movie_genre')
    summernote_fields = ('content')
    actions = ['approve_movies']

    def approve_movies(self, request, queryset):
        # Function to approve newly added movies
        queryset.update(movie_approved=True)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    # Defines the fields visible in Admin panel for the Review model

    list_display = (
        'reviewed_movie', 'author', 'review_rating', 'review_created_on'
        )
    search_fields = ('author', 'content')
    list_filter = ('review_rating', 'review_created_on')


@admin.register(WatchlistItem)
class WatchlistItemAdmin(SummernoteModelAdmin):
    # Defines the fields visible in Admin panel for the Watchlist model

    summernote_fields = ('content')


@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):
    # Defines the fields visible in Admin panel for the Genre model

    # From Django Slug Tutorial:
    prepopulated_fields = {'slug': ['genre_name']}
    list_filter = ['genre_name']
    list_display = ('genre_name', 'slug')
