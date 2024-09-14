from django.contrib import admin
from django.urls import path
from project_management_app.views import UserCardAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user_card_list/', UserCardAPIView.as_view(), name='user_card_list'),
]
