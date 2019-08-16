from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import BookMark


# Create your views here.

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: BookMark
        fields: ('lat', 'lon', 'user_id')

class BookmarkView(APIView):
    def get(self, request, format=None):
        print("Get received for Bookmart Now")
        BookmarkSerializer()
        return Response()