from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator


class ArticleView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            article = get_object_or_404(
                Article.objects
                .select_related('author', 'category')
                .prefetch_related('comments')
                .annotate(likes_count=Count('article_likes')),
                pk=pk
            )
            serializer = ArticleSerializer(article, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        articles = (
            Article.objects
            .select_related('author', 'category')
            .annotate(likes_count=Count('article_likes'))
        )
        serializer = ArticleListSerializer(articles, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            article, created = serializer.save()
            if created:
                    return Response(
                        {"detail": "Article created successfully", "article_id": article.id},
                        status=status.HTTP_201_CREATED,
                    )
            else:
                return Response(
                    {"detail": "Article updated successfully", "article_id": article.id},
                    status=status.HTTP_200_OK,
                )
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if not pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        article = get_object_or_404(Article.objects.filter(author=request.user).select_related("author").only("id","author"), pk=pk)
        article.delete()
        return Response({"detail": "Article deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class CommentView(APIView):
    def post(self, request, pk): # pk for article
        article = get_object_or_404(Article.objects.only('id'), pk=pk)
        if Comment.objects.filter(article=article, author=request.user).exists():
            return Response({"detail": "You have already commented on this article."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save(article=article, author=request.user)
            return Response({"detail": "Comment created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk): # pk for comment
        comment = get_object_or_404(Comment.objects.filter(author=request.user).select_related("author").only('id', "author"), pk=pk)
        comment.delete()
        return Response({"detail": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class LikeView(APIView):
    def post(self, request, pk):  # pk for article
        article = get_object_or_404(Article.objects.only('id'), pk=pk)

        # Try to delete the like if it exists, otherwise create it
        like_deleted, _ = Like.objects.filter(article=article, user=request.user).delete()

        if like_deleted:
            return Response({"detail": "Like deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        Like.objects.create(article=article, user=request.user)
        return Response({"detail": "Like created successfully"}, status=status.HTTP_201_CREATED)




class UserDetailView(APIView):
    """
    API view to retrieve a user's details along with their articles.
    """
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)