from updateme.views import new_business
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

    def test_create_business(self):
        self.business.create_business()
        bus1=Business.objects.all()
        self.assertFalse(len(bus1)>0)
