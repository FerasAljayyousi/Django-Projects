from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from drfapp.models import Studant
from drfapp.serializers import StudantSerializer
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Studant.objects.all()
        Studant1 = qs.first()
        serializer = StudantSerializer(Studant1)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)