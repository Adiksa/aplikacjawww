from rest_framework import serializers
from .models import Silnik
from .models import Modele
from django.contrib.auth.models import User

class SilnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silnik
        fields = '__all__'

class ModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = '__all__'

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','last_login','username','email','date_join']