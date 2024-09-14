from rest_framework import generics

from .models import UserCard
from .serializers import UserCardSerializer


class UserCardAPIView(generics.ListAPIView):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
