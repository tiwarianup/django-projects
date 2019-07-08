from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
from .models import UserProfile

User = get_user_model()

class UserProfileTestCase(TestCase):
    
    def setUp(self):
        self.username = 'someUser'
        newUser = User.objects.create(username=self.username)

    def test_profileCreated(self):
        username = self.username
        userProfile = UserProfile.objects.filter(user__username=self.username)
        self.assertTrue(userProfile.exists())
        self.assertTrue(userProfile.count() == 1)

    def test_newUser(self):
        newUser = User.objects.create(username=self.username+'ada')
