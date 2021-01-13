from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Silnik
from .models import Modele
from .serializers import ModeleSerializer
from .serializers import SilnikSerializer
from .serializers import UserSerializer
from rest_framework import permissions

class SilnikList(generics.ListCreateAPIView):
    queryset = Silnik.objects.all()
    serializer_class = SilnikSerializer
    name = 'silniks'
    search_fields = ['kod']
    ordering_fields = ['kod','moc','odciecieObrotow']
    filter_fields = ['kod','moc','odciecieObrotow']
    permission_classes = [permissions.IsAuthenticated]

class ModeleList(generics.ListCreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer
    name = 'modeles'
    search_fields = ['nazwa','nadwozie','silnik']
    ordering_fields = ['nazwa','nadwozie','silnik']
    filter_fields = ['nazwa','nadwozie','silnik']
    permission_classes = [permissions.IsAuthenticated]

class SilnikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Silnik.objects.all()
    serializer_class = SilnikSerializer
    name = 'silnik'
    permission_classes = [permissions.IsAuthenticated]

class ModeleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer
    name = 'modele'
    permission_classes = [permissions.IsAuthenticated]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users'
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user'
    permission_classes = [permissions.IsAuthenticated]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'silniks': reverse(SilnikList.name, request=request),
                         'modeles': reverse(ModeleList.name, request=request),
                         'users': reverse(UserList.name, request=request)
                         })