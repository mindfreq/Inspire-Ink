from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.ArticleView.as_view()),
    path('article/<uuid:pk>/', views.ArticleView.as_view()), # for Retrieve & Delete object
    
    path('comment/<uuid:pk>/', views.CommentView.as_view()),
    
    path('like/<uuid:pk>/', views.LikeView.as_view()),
    
    path('user/', views.UserDetailView.as_view()),
]
