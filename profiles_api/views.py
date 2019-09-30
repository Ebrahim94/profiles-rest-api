from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format = None):
        """returns a list of APIView features"""
        an_apiview = [
        'uses HTTP methods as function(get, post, patch, put, delete)',
        'is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URL',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
