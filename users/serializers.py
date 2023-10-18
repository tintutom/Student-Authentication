from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import Student


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'studentname', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.get('password')
        hashed_password = make_password(password)
        validated_data['password'] = hashed_password

        user = Student(**validated_data)
        user.save()
        return user

    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'studentname', 'email')

