from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Family
from data.serializers import FamilySerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all() # iterator
    serializer_class = FamilySerializer

    # custom rute made by me
    @action(detail=False)
    def filter_by_args(self, request, *args, **kwargs):
        edad = request.GET.get('edad')
        edad_new = int(edad)*10000
        return Response(edad_new)
