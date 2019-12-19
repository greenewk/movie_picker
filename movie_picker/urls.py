from django.urls import path
from movie_picker import views

app_name = 'movie_picker'
urlpatterns = [
    path('', views.home, name='home'),
    path('new_movie/', views.new_movie, name='new_movie'),

]
