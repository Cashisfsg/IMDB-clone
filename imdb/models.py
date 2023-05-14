from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg
from django.urls import reverse

from random import choice

from django.utils.timezone import now


class Director(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    portrait = models.ImageField(upload_to='directors/', null=True, blank=True)
    # movies
    # comments

    def __str__(self):
        return f'{self.first} {self.last}'

    def url_detail(self):
        return reverse('imdb:director-detail', kwargs={'pk': self.id})

    # def rating(self):
    #     movies = self.movies.all()
    #     if movies:
    #         return round(sum(movie.rating for movie in movies) / len(movies), 1)
    #     else:
    #         return 0

    def rating(self):
        return self.movies.all().aggregate(Avg('rating')).get('rating__avg')

    def trailer(self):
        trailers = [movie.trailer for movie in self.movies.all() if movie.trailer]
        if trailers:
            return choice(trailers)
        else:
            return None


class Movie(models.Model):
    title = models.CharField(max_length=256)
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(default=5.0)
    views = models.IntegerField(default=0)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    plot = models.FileField(upload_to='plots/', null=True, blank=True)
    trailer = models.CharField(max_length=12, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    # comments
    subscribers = models.ManyToManyField(User, related_name='watchlist', blank=True)

    def __str__(self):
        return self.title

    def url_detail(self):
        return reverse('imdb:movie-detail', kwargs={'slug': self.slug})


class UserAddon(models.Model):
    user = models.OneToOneField(User, related_name='addon', on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='user_avatars/', null=True, blank=True)


class MovieComment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    published = models.DateTimeField(default=now)