from rest_framework import serializers
from .models import User, UserPayment
class UserSerializer(serializers.ModelSerializer):
    class  Meta:
        model = User
        fields= '__all__'

class  PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields= '__all__'