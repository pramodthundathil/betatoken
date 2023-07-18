from rest_framework import serializers
from .models import Call_Tokens
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class Call_Taken_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Call_Tokens
        fields = "__all__"
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token