from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSite(TestCase):

    # The first thing we are going to do is create a setup function
    # which is a function that is run before every test. That is because
    # sometime there are setup tasks that need to be run before every test
    # in our test class
    def setUp(self):
        # create test client, add new user, make sure the user is logged in
        # to our client. Also create a regural user that is not authenticated
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@bourgosnet.com',
            password='password1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='testuser@bourgosnet.com',
            password='testpassword1234',
            name='Test user full name',
        )

    # we are gonna test that the users are listed in the django admin
    def test_users_listed(self):
        """Test that users are listed on user page"""
        # create the url using the reverse helper function
        url = reverse('admin:core_user_changelist')
        # the below will use our test client to perform a HTTP GET request
        # on the above URL
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # the reverse function will create the url /admin/core/user/{id}
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user works!"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
