from django.urls import path
from . import views

app_name ='movieapp'
urlpatterns = [
    path('', views.movielist, name='movielist'),
    path('moviedetail/<int:movie_id>/', views.moviedetail, name='moviedetail'),
    path('movieadd/', views.movieadd, name='movieadd'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]