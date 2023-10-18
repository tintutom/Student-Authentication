from django.urls import path
from users.views import RegisterView,MyTokenObtainPairView,RetrieveStudentView


urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/', MyTokenObtainPairView.as_view()),
    path('me/', RetrieveStudentView.as_view()),
]