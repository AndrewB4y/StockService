from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserCreationSerializer(serializers.ModelSerializer):
    
    username = None
    name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'name', 'last_name', 'email', 'password']
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email already exists")

        return super().validate(attrs)
    
    def create(self,validated_data):
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user