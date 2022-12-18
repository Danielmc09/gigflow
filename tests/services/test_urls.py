from django.test import SimpleTestCase
from django.urls import reverse, resolve

from app.services.views import *


# It tests the urls.py file.
class TestUrls(SimpleTestCase):

    def test_list_url_aspirante(self):
        """
        It tests the url of the view.
        """
        url = reverse('services:services')
        self.assertEqual(resolve(url).func.view_class, ServicesList)

    def test_update_url_aspirante(self):
        """
        The test_update_url_aspirante function tests that the url for the ServicesDetail view is correct
        """
        url = reverse('services:service', args=['1'])
        self.assertEqual(resolve(url).func.view_class, ServicesDetail)
