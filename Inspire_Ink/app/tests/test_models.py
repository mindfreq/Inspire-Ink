from django.test import TestCase
from django.contrib.auth import get_user_model
from app.models import Category, Tag, Article, Comment, Like, Notification

User = get_user_model()

class BlogModelsTest(TestCase):

    def setUp(self):
        """
        Set up test data for all the models.
        """
        self.user1 = User.objects.create_user(username="testuser1", password="password123", bio="Bio for user1")
        self.user2 = User.objects.create_user(username="testuser2", password="password123")

        self.category = Category.objects.create(name="Technology", description="All about tech.")

        self.tag1 = Tag.objects.create(name="Python")
        self.tag2 = Tag.objects.create(name="Django")

        self.article = Article.objects.create(
            author=self.user1,
            title="Test Article",
            content="This is a test article.",
            category=self.category,
        )
        self.article.tags.add(self.tag1, self.tag2)

        # Create comment
        self.comment = Comment.objects.create(
            article=self.article,
            author=self.user2,
            content="This is a test comment."
        )

        # Create like
        self.like = Like.objects.create(user=self.user2, article=self.article)

        # Create notification
        self.notification = Notification.objects.create(
            recipient=self.user1,
            content="You have a new like on your article."
        )

    def test_user_creation(self):
        """
        Test the User model and its additional fields.
        """
        self.assertEqual(self.user1.bio, "Bio for user1")
        self.assertEqual(self.user1.followers.count(), 0)

    def test_category_creation(self):
        """
        Test the Category model.
        """
        self.assertEqual(self.category.name, "Technology")
        self.assertEqual(self.category.description, "All about tech.")

    def test_tag_creation(self):
        """
        Test the Tag model.
        """
        self.assertEqual(Tag.objects.count(), 2)
        self.assertIn(self.tag1, self.article.tags.all())

    def test_article_creation(self):
        """
        Test the Article model.
        """
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.author, self.user1)
        self.assertEqual(self.article.category, self.category)
        self.assertEqual(self.article.tags.count(), 2)

    def test_comment_creation(self):
        """
        Test the Comment model.
        """
        self.assertEqual(self.comment.article, self.article)
        self.assertEqual(self.comment.author, self.user2)
        self.assertEqual(self.comment.content, "This is a test comment.")

    def test_like_creation(self):
        """
        Test the Like model.
        """
        self.assertEqual(self.like.user, self.user2)
        self.assertEqual(self.like.article, self.article)
        self.assertIsNone(self.like.comment)

    def test_notification_creation(self):
        """
        Test the Notification model.
        """
        self.assertEqual(self.notification.recipient, self.user1)
        self.assertEqual(self.notification.content, "You have a new like on your article.")
        self.assertFalse(self.notification.is_read)

    def test_article_view_increment(self):
        """
        Test manually incrementing the views for an article.
        """
        self.article.views += 1
        self.article.save()
        self.assertEqual(self.article.views, 1)

    def test_followers(self):
        """
        Test the followers functionality.
        """
        self.user1.followers.add(self.user2)
        self.assertEqual(self.user1.followers.count(), 1)
        self.assertIn(self.user2, self.user1.followers.all())
