from django.shortcuts import render
from django.views import generic
from .models import Movie


def index(request):
    """
    View to return index.html as home page
    """
    return render(request, 'index.html')


class MovieList(generic.ListView):
    model = Movie
    queryset = Movie.objects.order_by('-movie_created_on')
    template_name = 'index.html'
    # limiting number of posts that can appear on Movie page:
    paginate_by = 8
