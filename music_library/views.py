from re import T
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Music_LibrarySerializer
from .models import Music_Library

# Create your views here.
@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        lists = Music_Library.objects.all()
        serializer = Music_LibrarySerializer(lists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Music_LibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def song_details(request, pk):
    song = get_object_or_404(Music_Library, pk=pk)
    if request.method == 'GET':
        serializer = Music_LibrarySerializer(song);
        return Response(serializer.data)
    elif request.method == 'PUT':
        song = get_object_or_404(Music_Library, pk=pk)
        serializer = Music_LibrarySerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
