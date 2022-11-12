from django.shortcuts import render
from .serialaizers import NotesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notes
# Create your views here.
@api_view(['GET'])
def NoteView(request):
    notes=Notes.objects.all()
    serializer=NotesSerializer(notes,many=True)
    return Response(serializer.data)
#CreateView
@api_view(['POST'])
def CreateView(request):
    serializer=NotesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()       
    return Response(serializer.data)
# DetailView
@api_view(['GET'])
def DetailView(request,pk):
    notes = Notes.objects.get(id=pk)
    serializer = NotesSerializer(notes, many=False)
    return Response(serializer.data)
#UpdateView
@api_view(['POST'])
def UpdateView(request,pk):
    notes = Notes.objects.get(id=pk)
    serializer = NotesSerializer(instance=notes,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#DeleteView
@api_view(['DELETE'])
def deleteView(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response('Item successfully deleted!')
