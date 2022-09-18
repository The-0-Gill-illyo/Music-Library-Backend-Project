from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Music_LibrarySerializer
from .models import Music_Library

# Create your views here.
@api_view(['GET'])
def music_list(request):
    lists = Music_Library.objects.all()

    serializer = Music_LibrarySerializer(lists, many=True)

    return Response(serializer.data)

