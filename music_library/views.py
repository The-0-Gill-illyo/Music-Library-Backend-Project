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

@api_view(['GET'])
def song_details(request, pk):
    try:
        song = Music_Library.objects.get(pk=pk)
        serializer = Music_LibrarySerializer(song);

        return Response(serializer.data)
    except Music_Library.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
