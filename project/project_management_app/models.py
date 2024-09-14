from django.core.exceptions import ValidationError
from django.db import models

def random_slug():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Skill(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slug()
        super().save(*args, **kwargs)


class UserCard(models.Model):
    CHOICES_grade = (
        ('student', 'student'),
        ('junior', 'junior'),
        ('junior+', 'junior+'),
        ('middle', 'middle'),
        ('senior', 'senior'),
        ('lead', 'lead++'),
    )
    user = models.OneToOneField('auth_app.User', on_delete=models.CASCADE, blank=True)
    skills_user = models.ManyToManyField(Skill, blank=True)
    country = models.CharField(max_length=100, blank=True) #на удаление
    city = models.CharField(max_length=100) #на удаление
    telegram_id = models.CharField(max_length=100) #на удаление
    grade = models.CharField(max_length=100, choices=CHOICES_grade, blank=True)
    # github = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField(upload_to='user_images', blank=True)

    def save(self, *args, **kwargs):
        if not self.country:
            self.country = self.user.country
        super().save(*args, **kwargs)

# class Application_to_user_card(models.Model):
#     for_card = models.ForeignKey('User_card', on_delete=models.CASCADE)
#     to_card = models.ForeignKey('auth_app.User', on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     checked = models.BooleanField(default=False)