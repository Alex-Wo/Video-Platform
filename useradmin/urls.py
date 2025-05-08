from django.urls import path
from useradmin import views


urlpatterns = [
    path('', views.studio, name='studio'),
    path('video_delete/<vid>/', views.video_delete, name='video-delete')
]
