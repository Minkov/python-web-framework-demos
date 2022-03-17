from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from testing_demos.web.models import Profile
from testing_demos.web.views import ProfilesListView

UserModel = get_user_model()


class ProfilesListViewTests(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('list profiles'))

        self.assertTemplateUsed(response, 'profiles/list.html')

    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        # Arrange
        profiles_to_create = (
            Profile(first_name='Doncho', last_name='Minkov', age=15),
            Profile(first_name='Minko', last_name='Donchev', age=17),
        )
        Profile.objects.bulk_create(profiles_to_create)

        # Act
        response = self.client.get(reverse_lazy('list profiles'))

        # Assert
        profiles = response.context['object_list']
        # Check for actual profiles
        self.assertEqual(len(profiles), 2)

    def test_get__when_not_logged_in_user__expect_context_user_to_be_No_user(self):
        response = self.client.get(reverse('list profiles'))
        self.assertEqual(
            ProfilesListView.no_logged_in_user_value,
            response.context[ProfilesListView.context_user_key],
        )

    def test_get__when_logged_in_user__expect_context_user_to_be_username(self):
        user_data = {
            'username': 'doncho',
            'password': 'doncho123',
        }

        UserModel.objects.create_user(**user_data)

        self.client.login(**user_data)

        response = self.client.get(reverse('list profiles'))

        self.assertEqual(
            user_data['username'],
            response.context[ProfilesListView.context_user_key],
        )
