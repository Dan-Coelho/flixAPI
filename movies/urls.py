from django.urls import path
from . import views


urlpatterns = [
    path("movies/", views.MovieListCreateView.as_view(), name="movie_create_list"), 
    path("movies/<int:pk>/", views.MovieRetrieveUpdateDestroyView.as_view(), name="movie_detail"),
    path("movies/stats/", views.MovieStatsView.as_view(), name="movie_stats"),  # New endpoint for stats
]
