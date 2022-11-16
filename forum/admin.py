from django.contrib import admin
from .models import Movie, Review, WatchlistItem, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Movie)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


@admin.register(WatchlistItem)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


@admin.register(Genre)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
