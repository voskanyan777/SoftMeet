from django.contrib import admin
from django.urls import path
from project_management_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user-cards/lists', UserCardAPIView.as_view(), name='user_card_list'),
    path('api/v1/user-cards/create', CreateUserCardAPIView.as_view())
]
