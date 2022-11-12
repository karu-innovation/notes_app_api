from django.urls import path
from .views import NoteView,CreateView,UpdateView,deleteView,DetailView

app_name='notes_app'

urlpatterns=[
    path('',NoteView,name='notes'),
    path('create/',CreateView,name='create'),
    path('detail/<int:pk>/',DetailView,name='detail'),
    path('update/<int:pk>/',UpdateView,name='update'),
    path('delete/<int:pk>/',deleteView,name='delete'),
]