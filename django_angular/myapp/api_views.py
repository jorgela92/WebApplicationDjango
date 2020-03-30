from rest_framework import viewsets
from .models import Register
from .serializers import RegisterSerializer

class RegisterViewset(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer