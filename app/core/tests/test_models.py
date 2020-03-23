from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    # testing whether the email and password were registered correctly
    def test_create_user_with_email_successful(self):
        """Test Creating a new user with an email is successful"""
        email = 'test@bourgosnet.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    # we want the email to be registered as lower case even if the user
    # entered upper case
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@BOURGOSNET.COM'
        user = get_user_model().objects.create_user(email, 'test1234')
        # I have already tested the password I don't have to test it again
        # and that is why I am passing a simple string without encryption
        self.assertEqual(user.email, email.lower())

    # we want the user to always provide an email
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            # anything we run in here should raise a ValueError. If it doesn't
            # raise a ValueError then this test will fail
            get_user_model().objects.create_user(None, 'test1234')

    # test that when we call create_superuser, a superuser is created and that
    # is assigned the is_staff and is_superuser settings
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@bourgosnet.com',
            'password1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
