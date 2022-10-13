from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('edit/<int:tweet_id>/',views.Edit, name='edit'),
    path('likes/<int:tweet_id>/',views.like, name='like'),
    path('deleted/<int:tweet_id>/',views.delete, name='delete'),
]