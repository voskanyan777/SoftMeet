from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.context_processors import request


# class Сity(models.Model):
#     CHOICES_COUNTRY = (
#         ('UA', 'Ukraine'),
#         ('RU', 'Russia'),
#         ('US', 'USA'),
#     )
#     name = models.CharField(max_length=100)
#     country = models.CharField(max_length=100, blank=True, choices=CHOICES_COUNTRY)


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

class User(AbstractUser):
    CHOICES_COUNTRY = (
        ('UA', 'Ukraine'),
        ('RU', 'Russia'),
        ('US', 'USA'),
    )
    timezone = models.CharField(max_length=100, blank=True, default='')
    ip = models.CharField(max_length=100, blank=True, default='0.0.0.0')
    country = models.CharField(max_length=100, blank=True, choices=CHOICES_COUNTRY)

    telegram_id = models.CharField(max_length=100, blank=True)

    user_permissions = models.ManyToManyField('auth.Permission', related_name='user_permission', related_query_name='permission', blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='user_group', related_query_name='group', blank=True)

    def __str__(self):
        return '' + self.username + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)