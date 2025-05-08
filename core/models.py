from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

User = settings.AUTH_USER_MODEL

VISIBILITY = (
    ('private', 'Private'),
    ('unlisted', 'Unlisted'),
    ('members_only', 'Members Only'),
    ('public', 'Public')
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Video(models.Model):
    video = models.FileField(upload_to=user_directory_path, verbose_name='Видео')
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name='Превью')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    tags = TaggableManager(verbose_name='Теги')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    visibility = models.CharField(choices=VISIBILITY, max_length=100, default='public', verbose_name='Видимость')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    likes = models.ManyToManyField(User, related_name='likes', verbose_name='Лайки')
    featured = models.BooleanField(default=False, verbose_name='Рекомендовать?')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=10000, verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    active = models.BooleanField(default=True, verbose_name='Активен')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments', verbose_name='Видео')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __ste__(self):
        return self.comment[:30]
