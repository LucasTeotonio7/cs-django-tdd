from django.test import TestCase, RequestFactory
from animals.models import Animal


class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            name ='Lion',
            predator=True,
            venomous=False,
            domestic=False,
        )

    def test_animal_exists(self):
        self.assertEqual(self.animal.name, 'Lion')
