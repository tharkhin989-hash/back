from rest_framework import serializers
from .models import User,Category,Post,Comment,UserProfile,Tag,PostTag,PostLike

class UserSerializen(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class CategorySerializen(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class PostSerializen(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields ='__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields ='__all__'

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields ='__all__'