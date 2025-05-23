from django.shortcuts import render
from django.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Input
from .serializers import Input_Serializer

# Create your views here.

class Input_List_View(APIView):
    def get(self, request):
        inputs = Input.objects.all()
        serializer = Input_Serializer(inputs, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer =Input_Serializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    