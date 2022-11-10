from django.urls import path
from .views import NoteView

app_name='notes_app'

urlpatterns=[
    path('',NoteView,name='notes'),
]