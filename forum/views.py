from django.shortcuts import render, get_object_or_404
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


class MovieDetails(generic.ListView):
    """
    Displays movie object from Movie model &
    reviews posted on this object.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Gets full movie detail with approved reviews
        """
        queryset = Movie.objects.filter(movie_approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-review_created_on')

        return render(
            request,
            'forum/movie_detail.html',
            {
                'movie': movie,
                'reviews': reviews,
                'reviewed': False,
            },
        )


class GenreDetail(generic.View):
    """
    Returns all the movie objects from the Movie model
    filtered by a genre and with movie_approved = True
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get all the genre objects from the Genre model
        and the specific slug of the genre object
        Gets all the movie objects filtered then by
        their genre with movie_approved = True
        returns the single genre object instance,
        the movie object and the genre object list
        """

        genre_object = Genre.objects.all()
        genres = get_object_or_404(genre_object, slug=slug)
        movies = genres.movie_genre.filter(
            movie_approved=True).order_by('-movie_created_on')

        return render(
            request,
            'forum/genre.html',
            {
                'movies': movies,
                'genres': genres,
                'genre_object': genre_object
            },
        )
