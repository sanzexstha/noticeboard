from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.exceptions import PermissionDenied
from rest_framework import exceptions
from .permissions import *
from .serializers import (PostSerializer, UserSerializer, CommentSerializer, 
                        CommentListSerializer, PostLikeSerializer, )
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


class PostList(APIView):
    """
    List all posts ,create a new posts.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(posted_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         

class PostDetail(APIView):
    """
    Retrieve, delete, put posts
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise HTTP404
    
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):

        post = self.get_object(pk) 
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    """
    List all comments ,create a new comment.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request):
        comments = COment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(commented_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         

class CommentDetail(APIView):
    """
    Retrieve, delete, put comments
    """
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise HTTP404
    
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):

        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeList(APIView):
    """
    List all likes ,create a new like.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request):
        likes = PostLike.objects.all()
        serializer = PostLikeSerializer(likes, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = PostLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(liked_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

class LikeDetail(APIView):
    """
    delete a like
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return PostLike.objects.get(pk=pk)
        except PostLike.DoesNotExist:
            raise HTTP404
    

    def delete(self, request, pk):
        like = self.get_object(pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCreate(APIView):

    def post(self, request):

        """ API endpoint for creating/posting new user"""

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def post_list_post(request):
    
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
  
#     elif request.method == 'POST':
#         if request.user and request.user.is_authenticated:
#             serializer = PostSerializer(data=request.data)
            
      
#             if serializer.is_valid():
#                 serializer.save()
      
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
 
  

 
# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk):
#     """
#     views for retrieve, put and delete

#     """

#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         if request.user and request.user.is_authenticated:
#             serializer = PostSerializer(post, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


#     elif request.method == 'DELETE':
#         if request.user and request.user.is_authenticated:
#             post.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['GET', 'POST'])
# def comment_list_post(request):

#     """ API endpoint for listing all commments and posting """
    
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer =CommentListSerializer(comments, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         if request.user and request.user.is_authenticated:
#             serializer = CommentSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save(commented_by=request.user)
             
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def comment_detail(request, pk):

#     """ API endpoint for retrieve, patch and delete users' comments"""

#     try:
#         comment = Comment.objects.get(pk=pk)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CommentListSerializer(comment)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         if request.user and request.user.is_authenticated:
#             serializer = CommentSerializer(comment, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


#     elif request.method == 'DELETE':
#         if request.user and request.user.is_authenticated:
#             comment.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['GET', 'POST'])
# def like_list_post(request):

#     """API endpoint for GET and POST request for likes"""
    
#     if request.method == 'GET':
#         post_likes = PostLike.objects.all()
#         serializer = PostLikeSerializer(post_likes, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         if request.user and request.user.is_authenticated:
#             serializer = PostLikeSerializer(data=request.data)
           
      
#             if serializer.is_valid():
#                 serializer.save(liked_by=request.user)
                
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['GET', 'PUT', 'DELETE'])
# def like_detail(request, pk):

#     """ API endpoint for retrieve, update and delete""" 


#     try:
#         post_like = PostLike.objects.get(pk=pk)
#     except PostLike.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PostLikeSerializer(post_like)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         if request.user and request.user.is_authenticated:
#             post_like.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



# @api_view(['POST'])
# def user_create(request):
#     """ API endpoint for creating/posting new user"""

#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 