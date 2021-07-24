from django.test import TestCase
from .models import Business,Admin,NeighbourHood,User

# Create your tests here.
class BusinessTestClass(TestCase):
    #setup method
    def setUp(self):
        self.business=Business(name='cereals',email="a@gmail.com")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))