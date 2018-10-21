from django.shortcuts import render
from rest_framework import generics
from .serializers import ChismeSerializer
from .models import Chisme

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Chisme.objects.all()
    serializer_class = ChismeSerializer

    def crear_chisme(self,serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chisme.objects.all()
    serializer_class = ChismeSerializer
