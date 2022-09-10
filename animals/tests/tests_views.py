from django.db.models.query import QuerySet
from django.test import TestCase, RequestFactory
from animals.models import Animal


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            name ='Dog',
            predator=False,
            venomous=False,
            domestic=True,
        )

    def test_view_index_return_animal_characteristics(self):
        response = self.client.get('/',
            {'search' : 'Dog'}
        )
        researched_animal = response.context['characteristics']
        self.assertIs(type(response.context['characteristics']), QuerySet)
        self.assertEqual(researched_animal[0].name, 'Dog')

