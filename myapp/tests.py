 
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import *
from .serializers import *
 
class TestPost(TestCase):
     
              
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')
        self.user.save()

      
     
        self.client = APIClient()
        self.client.login(username='jacob', password='top_secret')

    def test_list(self):
        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)   

    def test_post(self):         
        with open('/home/sanjeev1/Desktop/test.jpg', 'rb') as image:
            
            response = self.client.post(reverse('post_list'), data= { 'image': image}, format='multipart')
            import ipdb
            ipdb.set_trace()           
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)   

    def test_put(self):
        