from django.shortcuts import render
from .serialaizers import NotesSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse  , HttpResponse
from rest_framework.response import Response
from .models import Notes
# Create your views here.

@api_view(['GET'])
def NoteView(request):
    note=Notes.objects.all()
    serializer=NotesSerializer(note,many=True)
    return Response(serializer.data)
