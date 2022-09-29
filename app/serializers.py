from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user