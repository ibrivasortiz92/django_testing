from django.test import TestCase
from .models import Post


class ModelTesting(TestCase):

  def setUp(self):
    self.blog = Post.objects.create(title = "Post 1", author = "User 1", slug = "Slug 1")

  def test_db(self):
    d = self.blog
    self.assertTrue(isinstance(d, Post))
    self.assertEqual(str(d), "Post 1")
