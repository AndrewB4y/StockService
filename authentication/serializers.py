from .models import User
from rest_framework import serializers

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