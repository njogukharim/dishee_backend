from django.shortcuts import render
from rest_framework import generics
from main.serializers import *
from main.models import *
from rest_framework.parsers import MultiPartParser, FormParser 


class UserListApiView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class OrderListApiView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class RecipeListApiView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    

class RecipeDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class CommentListApiView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

