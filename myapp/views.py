from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework import exceptions
from .permissions import *
from .serializers import (PostSerializer, UserSerializer, CommentSerializer, 
                        CommentListSerializer, PostLikeSerializer, )
 


@api_view(['GET', 'POST'])
def post_list_post(request):
    
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    
    
    elif request.method == 'POST':
        if request.user and request.user.is_authenticated:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(posted_by=request.user)
      
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
 
  

 
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    """
    views for retrieve, put and delete

    """

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user and request.user.is_authenticated:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


    elif request.method == 'DELETE':
        if request.user and request.user.is_authenticated:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET', 'POST'])
def comment_list_post(request):

    """ API endpoint for listing all commments and posting """
    
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer =CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user and request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(commented_by=request.user)
             
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):

    """ API endpoint for retrieve, patch and delete users' comments"""

    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentListSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user and request.user.is_authenticated:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)


    elif request.method == 'DELETE':
        if request.user and request.user.is_authenticated:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET', 'POST'])
def like_list_post(request):

    """API endpoint for GET and POST request for likes"""
    
    if request.method == 'GET':
        post_likes = PostLike.objects.all()
        serializer = PostLikeSerializer(post_likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.user and request.user.is_authenticated:
            serializer = PostLikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(liked_by=request.user)
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET', 'PUT', 'DELETE'])
def like_detail(request, pk):

    """ API endpoint for retrieve, update and delete""" 


    try:
        post_like = PostLike.objects.get(pk=pk)
    except PostLike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostLikeSerializer(post_like)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user and request.user.is_authenticated:
            post_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail':'authentication required'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def user_create(request):
    """ API endpoint for creating/posting new user"""

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 