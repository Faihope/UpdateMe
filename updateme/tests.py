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
        self.assertIsNotNone(bus1)

    def test_delete_business(self):
        self.business.create_business()
        business_record=Business.objects.all()
        self.business.delete_business()
        self.assertTrue(len(business_record)==0)
