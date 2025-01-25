from rest_framework import serializers
from .models import *
import os


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__" 
        read_only_fields = ["article", 'author', 'created_at']

        
     
class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    image = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Article
        fields = "__all__" 
        read_only_fields = ['created_at', 'updated_at']
        
        
    def get_image(self, obj):
        request = self.context.get('request') 
        if obj.thumbnail:
            return request.build_absolute_uri(obj.thumbnail.url) 
        return None
    
    def validate_thumbnail(self, value):
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in valid_extensions:
            raise serializers.ValidationError("JPG, JPEG, PNG, GIF, WebP.")
        return value
                
    def create(self, validated_data):
            """
            Override the create method to use update_or_create.
            """
            title = validated_data.get('title')
            defaults = {
                "introduction": validated_data.get('introduction'),
                "content": validated_data.get('content'),
                "author": self.context['request'].user,
                "category": validated_data.get('category'),
                "thumbnail": validated_data.get('thumbnail'),
            }
            article, created =  Article.objects.update_or_create(author=self.context['request'].user, title=title, defaults=defaults)
            return article, created
        
        
class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ["id", "author", "title", "image", "likes_count", 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        
    def get_image(self, obj):
        request = self.context.get('request') 
        if obj.thumbnail:
            return request.build_absolute_uri(obj.thumbnail.url) 
        return None
    
    
    
    
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model that includes the user's articles.
    """
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_image', 'followers', 'articles']