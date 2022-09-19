from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Music_LibrarySerializer
from .models import Music_Library


# Create your views here.
@api_view(['GET', 'POST'])
def music_list(request):
    try:
        if request.method == 'GET':
            lists = Music_Library.objects.all()
            serializer = Music_LibrarySerializer(lists, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = Music_LibrarySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)

@api_view(['GET', 'PUT', 'DELETE'])
def song_details(request, pk):
    try:
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
        elif request.method == 'DELETE':
            song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        print(err)
 
def liked_song(request):
    song = get_object_or_404(Music_Library, id=request.Music_Library.get('song_id'))
    song.likes.add(request.user)
    if request.method == 'POST':
        song = request.POST.get(song)
        
        return render(request, 'button_detail.html')

def disliked_song(request):
    song = get_object_or_404(Music_Library, id=request.Music_Library.get('song_id'))
    song.likes.add(request.user)
    if request.method == 'POST':
        song = request.POST.get(song)

    return render(request, 'button_detail.html')