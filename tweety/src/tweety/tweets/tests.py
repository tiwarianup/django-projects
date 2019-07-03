from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='heavenly')
        #Tweet.objects.create(author = User.objects.first(), tweetText = 'some new tweet for test')

    def test_TweetItem(self):
        obj = Tweet.objects.create(
            author = User.objects.first(),
            tweetText = 'some new tweet for test'
        )
        self.assertTrue(obj.tweetText == 'some new tweet for test')
        self.assertTrue(obj.id == 1)
        absoluteUrl = reverse("tweet:tweetDetailView", kwargs={'pk':1})
        self.assertEqual(obj.get_absolute_url(), absoluteUrl)

    def test_tweetUrl(self):
        obj = Tweet.objects.create(
            author = User.objects.first(),
            tweetText = 'some new tweet for test'
        )
        absoluteUrl = reverse("tweet:tweetDetailView", kwargs={'pk': obj.pk})
        self.assertEqual(obj.get_absolute_url(), absoluteUrl)