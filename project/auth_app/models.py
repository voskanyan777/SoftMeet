from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CHOICES_COUNTRY = (
        ('UA', 'Ukraine'),
        ('RU', 'Russia'),
        ('US', 'Пендосия'),
    )
    timezone = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True, choices=CHOICES_COUNTRY)

    user_permissions = models.ManyToManyField('auth.Permission', related_name='user_permission', related_query_name='permission', blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='user_group', related_query_name='group', blank=True)

    def __str__(self):
        return '' + self.username + ' ' + self.last_name