from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    """
    Represents a user of the blog application. Extends the default Django AbstractUser to include additional fields.
    """
    bio = models.TextField(null=True, blank=True, help_text="A short biography of the user.")
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True, help_text="Profile image of the user.")
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True, help_text="Users who follow this user.")

    def __str__(self):
        """Returns the username of the user."""
        return self.username



class Article(models.Model):
    """
    Represents an article written by a user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles", help_text="The author of the article.")
    title = models.CharField(max_length=50, help_text="The title of the article.")
    introduction = models.CharField(max_length=300, help_text="The introduction of the article.")
    content = models.TextField(null=True, blank=True, help_text="The content of the article.")
    thumbnail = models.ImageField(upload_to="article_thumbnails/", null=True, blank=True, help_text="An optional thumbnail image for the article.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The timestamp when the article was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The timestamp when the article was last updated.")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="articles", help_text="The category of the article.")

    def __str__(self):
        """Returns the title of the article."""
        return self.title


class Category(models.Model):
    """
    Represents a category to organize articles.
    """
    name = models.CharField(max_length=100, unique=True, help_text="The unique name of the category.")
    description = models.TextField(null=True, blank=True, help_text="A short description of the category.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The timestamp when the category was created.")

    def __str__(self):
        """Returns the name of the category."""
        return self.name
    

class Comment(models.Model):
    """
    Represents a comment on an article.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", help_text="The article this comment belongs to.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", help_text="The author of the comment.")
    content = models.TextField(help_text="The content of the comment.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The timestamp when the comment was created.")

    def __str__(self):
        """Returns a short description of the comment."""
        return f"Comment by {self.author.username} on {self.article.title}"


class Like(models.Model):
    """
    Represents a like for an article or a comment.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes", help_text="The user who liked the article or comment.")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_likes", null=True, blank=True, help_text="The article that was liked, if applicable.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The timestamp when the like was created.")

    def __str__(self):
        """Returns a short description of the like."""
        if self.article:
            return f"{self.user.username} liked {self.article.title}"
        elif self.comment:
            return f"{self.user.username} liked a comment"


class Notification(models.Model):
    """
    Represents a notification for a user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications", help_text="The user who will receive the notification.")
    content = models.CharField(max_length=255, help_text="The content of the notification.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The timestamp when the notification was created.")
    is_read = models.BooleanField(default=False, help_text="Indicates whether the notification has been read.")

    def __str__(self):
        """Returns a short description of the notification."""
        return f"Notification for {self.recipient.username}"


class View(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="views")
    id_address = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"View on {self.article.title}"