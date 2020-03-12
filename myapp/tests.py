 
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import *
from .serializers import *
from django.core.files.images import ImageFile
from PIL import Image
import tempfile


 
class TestPost(TestCase):
           
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')
        self.post = Post.objects.create(posted_by=self.user, text='tes' )  

        self.client = APIClient()
        self.client.login(username='jacob', password='top_secret')

    def test_list(self):
        response = self.client.get(reverse('post_list'))
    

        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_post(self):   
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)      
        with open(tmp_file.name, 'rb') as image:
            
            response = self.client.post(reverse('post_list'), data= { 'text':'sanjev','image': image}, format='multipart')
              
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
            self.assertEqual(response.data.get('text'),  'sanjev')
 
    def test_retrieve(self):

        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.data.get('id'), self.post.id)


    def test_put(self):
        image = Image.new('RGB', (101, 101))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file) 
           
        with open(tmp_file.name, 'rb') as image:
            response = self.client.put(
                reverse('post_detail',  kwargs={'pk': self.post.pk}),
                data= { 'text':'sanjev','image': image},  
                format='multipart'        
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(
        reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        

        