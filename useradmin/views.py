from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from channel.models import Channel
from core.models import Video


@login_required
def studio(request):
    user = request.user
    channel = Channel.objects.get(user=user)
    videos = Video.objects.filter(user=user)

    context = {
        'user': user,
        'channel': channel,
        'videos': videos,
    }

    return render(request, 'useradmin/studio.html', context)


def video_delete(request, vid):
    user = request.user
    video = Video.objects.get(id=vid, user=user)
    video.delete()
