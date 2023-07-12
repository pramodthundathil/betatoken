from rest_framework import serializers
from .models import Call_Tokens

class Call_Taken_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Call_Tokens
        fields = "__all__"