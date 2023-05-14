import json

from django.contrib.auth import logout, authenticate, login
from django.core.serializers import serialize
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from .forms import *


class IndexView(ListView):
    model = Director
    template_name = 'imdb/index.html'
    queryset = Director.objects.annotate(rating_avg=Avg('movies__rating')).order_by('-rating_avg')[:6]
    context_object_name = 'directors'
    extra_context = {
        'movies': Movie.objects.all()[:6],
    }


class MovieDetail(DetailView):
    model = Movie
    extra_context = {
        'mcf': MovieCommentForm(),
    }


class DirectorList(ListView):
    model = Director
    context_object_name = 'directors'
    queryset = Director.objects.order_by('last', 'first')


class DirectorDetail(DetailView):
    model = Director


class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'
    queryset = Movie.objects.order_by('title')
    paginate_by = 6


def search(request):
    query = request.GET.get('query')
    if query:
        movies = Movie.objects.filter(title__icontains=query).order_by('title').values('id',
                                                                                       'title',
                                                                                       'year',
                                                                                       'director__first',
                                                                                       'director__last',
                                                                                       'poster',
                                                                                       'slug')[:3]
        return JsonResponse({'movies': list(movies)})
    else:
        return JsonResponse({'movies': []})


def search_list(request):
    query = request.POST.get('query').strip()
    url = request.GET.get('next')
    if query:
        context = {
            'query': query,
            'movies': Movie.objects.filter(title__icontains=query).order_by('title'),
            'directors': Director.objects.filter(Q(last__icontains=query) | Q(first__icontains=query)).order_by('last', 'first')
        }
        return render(request, template_name='imdb/search_list.html', context=context)
    else:
        return HttpResponseRedirect(url)


def user_sign_in(request):
    url = request.GET.get('url')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(url)


def user_sign_out(request):
    url = request.GET.get('url')
    logout(request)
    return HttpResponseRedirect(url)


def add_new_comment(request, pk):
    movie = Movie.objects.get(pk=pk)
    author = request.user
    form = MovieCommentForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data.get('text')
        MovieComment.objects.create(text=text, author=author, movie=movie)
    else:
        print(form.errors.as_json())
    return HttpResponseRedirect(movie.url_detail())


def change_watchlist(request, pk):
    movie = Movie.objects.get(pk=pk)
    user = request.user
    if user in movie.subscribers.all():
        movie.subscribers.remove(user)
    else:
        movie.subscribers.add(user)
    return HttpResponseRedirect(movie.url_detail())

