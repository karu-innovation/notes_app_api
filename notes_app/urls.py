from django.urls import path
from .views import NoteView,CreateView,UpdateView,deleteView

app_name='notes_app'

urlpatterns=[
    path('',NoteView,name='notes'),
    path('create/',CreateView,name='create'),
    path('update/<int:pk>/',UpdateView,name='update'),
    path('delete/<int:pk>/',deleteView,name='delete'),
]