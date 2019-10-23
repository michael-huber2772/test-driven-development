from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # resolve checks that the url "/" finds the view home_page
        self.assertEqual(found.func, home_page)
