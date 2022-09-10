from django.db.models.query import QuerySet
from django.test import TestCase, RequestFactory


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_view_index_return_animal_characteristics(self):
        response = self.client.get('/',
            {'characteristics' : 'result'}
        )
        self.assertIs(type(response.context['characteristics']), QuerySet)

