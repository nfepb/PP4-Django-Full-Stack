from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Avg


class Movie(models.Model):
    """
    Movie Class model
    """
    movie_title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    directors = models.CharField(max_length=200)
    year_released = models.DateField()
    synopsis = models.TextField()
    movie_poster = CloudinaryField('image', default='placeholder')
    movie_created_on = models.DateTimeField(auto_now_add=True)
    movie_updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order our movies based on decreasing average rating order
        """
        # TO BE MODIFIED BY "-average_rating"
        ordering = ['-movie_created_on']

# Return String representation in Django doc:
    def __str__(self):
        return self.movie_title


RATING = (
    (0, "Not to prioritise"),
    (1, "Entertaining"),
    (2, "Must watch")
    )


class Review(models.Model):
    """
    Review Class model
    """
    reviewed_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_reviews"
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name="review_author"
        )
    content = models.TextField()
    review_rating = models.IntegerField(choices=RATING, default=1)
    review_created_on = models.DateTimeField(auto_now_add=True)
    review_updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="review_likes", blank=True
        )

    class Meta:
        ordering = ['-review_created_on', '-review_updated_on']

    def __str__(self):
        return f"Review by {self.author}: {self.content} - rating:{self.review_rating}"


class WatchlistItem(models.Model):
    """
    WatchlistItem Class model
    """
    watchlistItem_movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_watchlist"
        )
    watchlistItem_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_watchlist"
        )
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return f"Review by {self.author}: {self.content} - rating:{self.review_rating}"


class Genre(models.Model):
    """
    Genre Class Model
    """
    genre_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genre_name
