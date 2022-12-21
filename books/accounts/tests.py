from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'john',
            email = 'john@email.com',
            password = 'testpass1'
        )
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'john@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)