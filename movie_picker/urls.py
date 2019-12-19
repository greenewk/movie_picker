from django.urls import path
from . import views
from django.urls import include

app_name = 'movie_picker'
urlpatterns = [
    path('', views.home, name='home'),
    path('new_movie/', views.new_movie, name='new_movie'),
    path('accounts/', include('django.contrib.auth.urls')),


]
