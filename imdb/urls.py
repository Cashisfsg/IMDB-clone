from django.urls import path

from . import views

app_name = 'imdb'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('director/list/', views.DirectorList.as_view(), name='director-list'),
    path('movie/list/', views.MovieList.as_view(), name='movie-list'),
    path('movie/<slug:slug>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('director/<int:pk>/', views.DirectorDetail.as_view(), name='director-detail'),
    path('search', views.search, name='search'),
    path('search/list/', views.search_list, name='search-list'),
    path('user/sign/in/', views.user_sign_in, name='user-sign-in'),
    path('user/sign/out/', views.user_sign_out, name='user-sign-out'),
    path('add/comment/<int:pk>/', views.add_new_comment, name='add-new-comment'),
    path('watchlist/change/<int:pk>/', views.change_watchlist, name='change-watchlist'),
]