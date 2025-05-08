from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import post_save

from django.conf import settings
from core.models import user_directory_path

User = settings.AUTH_USER_MODEL

STATUS = (
    ('active', 'Active'),
    ('disable', 'Disable'),
)


class Channel(models.Model):
    channel_art = models.ImageField(upload_to=user_directory_path, null=True, blank=True, default='channel-art.jpg',
                                    verbose_name='Фото канала')
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name='Аватар')
    full_name = models.CharField(max_length=200, verbose_name='Полное имя')
    channel_name = models.CharField(max_length=200, verbose_name='Название канала')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    keywords = TaggableManager(verbose_name='Теги')
    joined = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=100, default='active', verbose_name='Статус канала')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="channel",
                                verbose_name='Пользователь')
    subscribers = models.ManyToManyField(User, related_name='user_subs', verbose_name='Подписчики')
    verified = models.BooleanField(default=False, verbose_name='Подтверждён')
    total_views = models.IntegerField(default=0, verbose_name='Всего просмотров')
    business_email = models.EmailField(null=True, blank=True, verbose_name='Email')
    make_business_email_public = models.BooleanField(default=False, verbose_name='Видимость Email')
    business_location = models.CharField(null=True, blank=True, max_length=500, verbose_name='Юр. адрес')
    make_business_location_public = models.BooleanField(default=False, verbose_name='Видимость юр. адреса')
    website = models.URLField(default='https://my-website.com/', verbose_name='Веб-сайт')
    instagram = models.URLField(default='https://isntagram.com/')
    facebook = models.URLField(default='https://facebook.com/')
    twitter = models.URLField(default='https://twitter.com/')

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'

    def __str__(self):
        return self.channel_name

    def save(self, *args, **kwargs):
        if self.channel_name == '':
            self.channel_name = self.user.username
        super().save(*args, **kwargs)


def create_user_channel(instance, created, **kwargs):
    if created:
        Channel.objects.create(user=instance)


def save_user_channel(instance, **kwargs):
    instance.channel.save()


post_save.connect(create_user_channel, sender=User)
post_save.connect(save_user_channel, sender=User)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.channel.user.id, filename)


class Community(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name='Канал')
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True, verbose_name='Фото')
    content = models.TextField(null=True, blank=True, verbose_name='Содержимое поста')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=100, choices=STATUS, default='active', verbose_name='Статус канала')
    likes = models.ManyToManyField(User, verbose_name='Понравилось')

    class Meta:
        verbose_name = 'Пост сообщества'
        verbose_name_plural = 'Посты сообществ'

    def __str__(self):
        return self.channel.channel_name


class CommunityComment(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments',
                                  verbose_name='Сообщество')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment = models.CharField(max_length=10000, verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Комментарий сообщества'
        verbose_name_plural = 'Комменты сообществ'

    def __str__(self):
        return self.community.channel.channel_name
