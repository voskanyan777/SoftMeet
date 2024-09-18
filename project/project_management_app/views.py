from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserCard
from .serializers import UserCardSerializer


class UserCardAPIView(generics.ListAPIView):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer

class CreateUserCardAPIView(generics.CreateAPIView):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer


class UserCardUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(UserCard, pk=pk)
    
    def put(self, request, pk):
        user_card = self.get_object(pk=pk)
        serializer = UserCardSerializer(user_card, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user_card = self.get_object(pk)
        user_card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)