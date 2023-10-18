from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from users.serializers import StudentCreateSerializer, StudentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['studentname'] = user.studentname 
        token['email'] = user.email  
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        
        serializer = StudentCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.create(serializer.validated_data)
        user = StudentSerializer(user)

        return Response(user.data, status=status.HTTP_201_CREATED)

class RetrieveStudentView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user = StudentSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)
