from django.shortcuts import render
from django.views import generic
from .models import Movie, Review, WatchlistItem, Genre


def index(request):
    """
    View to return index.html as home page
    """
    return render(request, 'index.html')


class MovieList(generic.ListView):
    """
    Looks for Movie model and returns list:
    approved = True ordered by created date on home page
    """
    model = Movie
    queryset = Movie.objects.filter().order_by(
        '-movie_created_on'
        )
    template_name = 'index.html'
    # limiting number of posts that can appear on Movie page:
    paginate_by = 8

    def get_context_data(self, **kwargs):
        """
        Takes the genre object from Genre model
        and returns a list
        """
        context_data = super().get_context_data(**kwargs)
        context_data['genre_list'] = Genre.objects.all()
        return context_data


class WatchlistList(generic.ListView):
    """
    Looks for WatchlistItem model and returns list:
    movies approved = True ordered by added date on watchlist page
    """
    model = WatchlistItem
    queryset = WatchlistItem.objects.filter(
        ).order_by('-added_on')
    template_name = 'forum/watchlist.html'
    paginate_by = 12
    context_object_name = 'watchlist'
