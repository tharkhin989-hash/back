from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import *

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializen

class CategoryViewSet(viewsets.ModelViewSet):
     queryset =Category.objects.all()
     serializer_class = CategorySerializen

     
class PostViewSet(viewsets.ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializen

class CommentViewSet(viewsets.ModelViewSet):
    queryset =Comment.objects.all()
    serializer_class = CommentSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset =UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset =Tag.objects.all()
    serializer_class = TagSerializer

class PostTagViewSet(viewsets.ModelViewSet):
    queryset =PostTag.objects.all()
    serializer_class = PostTagSerializer

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset =PostLike.objects.all()
    serializer_class = PostLikeSerializer
# Create your views here.
