from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import User
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


        