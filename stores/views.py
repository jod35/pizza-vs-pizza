from django.shortcuts import render

# Create your views here.
from .models import Pizzeria
from .serializers import PizzeriaSerializer,PizzeriaDetailSerializer
from rest_framework import generics


class PizzeriaListView(generics.ListAPIView):
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaSerializer


class PizzeriaDetailView(generics.RetrieveAPIView):
    lookup_field="id"
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaDetailSerializer


class PizzeriaCreateView(generics.CreateAPIView):
    queryset=Pizzeria.objects.all()
    serializer_class=PizzeriaDetailSerializer


class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field="id"
    query_set=Pizzeria.objects.all()
    serializer_class=PizzeriaDetailSerializer



class PizzeriaDeleteView(generics.DestroyAPIView):
    lookup_field="id"
    query_set=Pizzeria.objects.all()
    

