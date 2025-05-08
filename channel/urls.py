from django.urls import path
from channel import views

urlpatterns = [
    path('<channel_name>/', views.channel_profile, name='channel-profile'),
    path('<channel_name>/video/', views.channel_videos, name='channel-videos'),
    path('<channel_name>/about/', views.channel_about, name='channel-about'),
    path('<channel_name>/community/', views.channel_community, name='channel-community'),
    path('<channel_name>/community/<int:community_id>', views.channel_community_detail,
         name='channel-community-detail'),
    path('community/<int:community_id>/create-comment/', views.create_comment, name='community-create-comment'),
    path('community/<int:community_id>/<int:comment_id>/', views.delete_comment, name='community-delete-comment'),
    path('community/<int:community_id>/like/', views.like_community_post, name='community-post-like'),
    path('channel/create/video/', views.video_upload, name='upload-video'),
    path('channel/edit-video/<channel_id>/<video_id>/', views.video_edit, name='video-edit'),
    path('channel/delete-video/<video_id>/', views.video_delete, name='video-delete'),
    path('channel/create-community-post/<channel_id>/', views.create_community_post, name='create-post'),
    path('channel/edit-community-post/<channel_id>/<community_post_id>/', views.edit_community_post, name='edit-post'),
    path('channel/delete-community-post/<channel_id>/<post_id>/', views.delete_comm_post, name='delete-post')
]
