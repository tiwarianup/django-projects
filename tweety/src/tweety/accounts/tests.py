from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
from .models import UserProfile

User = get_user_model()

class UserProfileTestCase(TestCase):