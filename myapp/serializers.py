from .models import *
from rest_framework import serializers




# class UserSerializer(serializers.ModelSerializer):

    

 

#     def to_internal_value(self, data):
#         user_data = data['user']
#         return super().to_internal_value(user_data)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'password')
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
 
class UserSerializer(serializers.Serializer):

    def to_internal_value(self, data):
        user_data = data('posted_by')
        return super().to_internal_value(user_data)

    username= serializers.CharField(max_length=100)
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

    comment = serializers.CharField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
 
 
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, validated_data):
        instance.comment=validated_data.get('comment', instance.comment)
        return instance

class CommentListSerializer(serializers.Serializer):
    commented_by = UserSerializer(read_only=True)
    comment = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    def create(self, validated_data):
        raise NotImplementedError
 

class PostLikeSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    liked = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return PostLike.objects.create(**validated_data)


class PostSerializer(serializers.Serializer):
    posted_by= serializers.ReadOnlyField(source='posted_by.username')

    text = serializers.CharField()
    posted_date = serializers.DateTimeField()

    image = serializers.ImageField()
    # post_likes = PostLikeSerializer(many=True, read_only=True)
    comments = CommentListSerializer(read_only=True, source='comment', many=True)


    def create(self, validated_data): 
        print(validated_data)
        return Post.objects.create(**validated_data)

    def update(self, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.image = validated_data.get('image', instance.image)
        return instance
        
        









# class PostSerializer(serializers.Serializer):
    
#     image = serializers.ImageField()

#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         user = User.objects.get(username=user_data.username)

#         return Post.objects.create(user=user, **validated_data)

#     def update(self, instance, validated_data):
#         instance.image=validated_data.get('image', instance.image)
#         return instance


