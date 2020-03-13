from .models import *
from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator

class DummyObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class UserSerializer(serializers.Serializer):

   
    id = serializers.ReadOnlyField()
    username= serializers.CharField(max_length=100, validators=[
        UnicodeUsernameValidator() ])
    password= serializers.CharField(max_length=100, write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
 
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        return user

    def update(self, instance, validated_data):
        instane.username =validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('username',  instance.first_name )
        instance.last_name=validated_data.get('username',  instance.last_name)
        return instance  


class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    comment = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
 
 
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment=validated_data.get('comment', instance.comment)
        return instance

class CommentListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    commented_by = UserSerializer(read_only=True)
    comment = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    def create(self, validated_data):
        raise NotImplementedError
 

class PostLikeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    liked_by = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    def create(self, validated_data):
        return PostLike.objects.create(**validated_data)
 


class PostLikeListSerializer(serializers.Serializer):
    liked_by = UserSerializer(read_only=True)
 


class PostSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)  
    image = serializers.ListField(
                    child=serializers.ImageField( max_length=100000,
                    allow_empty_file=False,
                    use_url=False ) 
                    )

    def create(self, validated_data):

        if not (validated_data.get('text') or validated_data.get('image')):
            raise serializers.ValidationError('Post is empty')
        else:
            img_data=validated_data.pop('image')
            post=Post.objects.create(**validated_data)
            for img in img_data:
                PostImage.objects.create(post=post,image=img)
            validated_data={**validated_data, **({'image': img_data})}
            return DummyObject(**validated_data)


    def update(self, instance, validated_data):
        print(instance)
        # instance.text = validated_data.get('text', instance.text)
        # post_image=instance.post_images
        # instance.image = validated_data.get('image', instance.image)
        return instance


class PostImageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    image=serializers.ImageField()


    def create(self, validated_data):
        raise NotImplementedError

    def update(self, validated_data):
        raise NotImplementedError


    
     

class PostListSerializer(serializers.Serializer):
      
    id = serializers.ReadOnlyField()
    posted_by= UserSerializer(read_only=True)
    text = serializers.CharField(required=False)  
    post_images = PostImageSerializer(many=True, read_only=True)
    posted_date = serializers.DateTimeField(read_only=True)
    post_likes = PostLikeListSerializer(many=True, read_only=True)
    comments = CommentListSerializer(read_only=True,source='post_comments', many=True)
            
    def create(self, validated_data):
        raise NotImplementedError

    def update(self, validated_data):
        raise NotImplementedError


 