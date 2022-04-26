from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

from profiles_api import models


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer  # Get functiion from serializer.py (Key item !!!)

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # Must return a dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})  # Must return a dictionary
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating/replacing an object"""

        return Response({'method': 'PUT'})  # Must return a dictionary

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})  # Must return a dictionary

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})  # Must return a dictionary


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles - Use this for databases e.g., CRUD"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
