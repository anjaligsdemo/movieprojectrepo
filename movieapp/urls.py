from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail_view, name='detail_view'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/update/<int:movie_id>/', views.updade_movie_details, name='updade_movie_details'),
    path('movie/delete/<int:movie_id>/', views.delete_movie_details, name='delete_movie_details'),
]
