from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer,PaymentSerializer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

class CreateUserView(APIView):
    def post(self, request) -> Response:
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data  # Use validated_data instead of data
            serializer.save()  # Save the validated data to the database
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, pk):
        try:
            user = User.objects.get(chat_id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise NotFound(detail="User not found")



class PaymentUserView(APIView):
    def post(self, request):  
        data = request.data.copy()  # Make a mutable copy of request.data
        chat_id = data.get('user')  # Get the chat_id from the request data
        try:
            user = User.objects.get(chat_id=chat_id)  # Retrieve the user object using chat_id
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        data['user'] = user.id  # Assign the user ID to the 'user' field in the data
        print(data)
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment created successfully", "data": serializer.data})
        return Response(serializer.errors)

