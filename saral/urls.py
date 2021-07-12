
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('movies/',views.movies, name='movies'),
    path('series/',views.series, name='series'),
    path('shows/',views.shows, name='shows'),
    path('watch/<int:pk>/',views.watch, name='watch'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logoutuser, name='logoutuser'),
    path('profile/',views.profile, name='profile'),
]
