
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Restaurant, Review

class RestaurantAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant_data = {
            'name': 'Test Restaurant',
            'address': '123 Test Address',
            'phone_number': '123-456-7890',
            'description': 'A test restaurant.'
        }
        self.restaurant = Restaurant.objects.create(**self.restaurant_data)

    def test_get_restaurant_list(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_restaurant(self):
        response = self.client.post('/restaurants/', self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_restaurant_detail(self):
        response = self.client.get(f'/restaurants/{self.restaurant.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_restaurant(self):
        updated_data = {
            'name': 'Updated Restaurant',
            'address': '456 Updated Address',
            'phone_number': '987-654-3210',
            'description': 'An updated restaurant.'
        }
        response = self.client.put(f'/restaurants/{self.restaurant.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_restaurant(self):
        response = self.client.delete(f'/restaurants/{self.restaurant.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ReviewAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test Address',
            phone_number='123-456-7890',
            description='A test restaurant.'
        )
        self.review_data = {
            'restaurant': self.restaurant.id,
            'rating': 5,
            'comment': 'Great restaurant!'
        }

    def test_create_review(self):
        response = self.client.post(f'/restaurants/{self.restaurant.id}/reviews/', self.review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
