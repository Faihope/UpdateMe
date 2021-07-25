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

    # def test_delete_business(self):
    #     self.business.create_business()
    #     business_record=Business.objects.all()
    #     self.business.delete_business()
    #     self.assertTrue(len(business_record)==0)

    def test_find_business(self):
        business=Business.objects.all()
        search_term='cereals'
        db_term=search_term
        if db_term !=search_term:
            return('no match')

        else:
            return(search_term) 

    def test_update_business(self):
        business=Business.objects.all()
        new_bus=Business.update_business(self)
        expected_business=f'{new_bus}'
        self.assertTrue(expected_business,'new_bus')

class NeighbourhoodTestClass(TestCase):
    #setup method
    def setUp(self):
        self.neighbourhood=NeighbourHood(name='sucess',location="kericho")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,NeighbourHood))

    def test_create_neighbourhood(self):
        new_neighbourhood=NeighbourHood.create_neighbourhood(self)
        neighbourhood1=f'{new_neighbourhood}'
        self.assertTrue(neighbourhood1,'new_neighbourhood')
