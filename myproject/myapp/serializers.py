from .models import *
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=100)
    password= serializers.CharField(max_length=100, write_only=True, required=False)
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100,  required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        return User

    def update(self, instance, validated_data):
        instane.username =validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('username',  instance.first_name )
        instance.last_name=validated_data.get('username',  instance.last_name)
        return instance  


class PostSerializer(serializers.Serializer):
    user = UserSerializer()
    image = serializers.ImageField()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.get(username=user_data.username)

        return Post.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.image=validated_data.get('image', instance.image)
        return instance


