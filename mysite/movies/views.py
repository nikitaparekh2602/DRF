from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviedata
from .seriallizers import MovieSerializer

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ__iexact='action') #This will allow your ComedyViewSet to match typ values like "Comedy", "COMEDY", or "comedy" (or any other variation of capitalization).
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ__iexact='comedy')
    serializer_class = MovieSerializer