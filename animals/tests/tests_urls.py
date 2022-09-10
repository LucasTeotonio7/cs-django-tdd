from urllib import response
from django.test import TestCase, RequestFactory
from django.urls import reverse

from animals.views import index

class AnimalsURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        return super().setUp()

    def test_route_use_view_index(self):
        "tests if the application uses the index function of the view"
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
