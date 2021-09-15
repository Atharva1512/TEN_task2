from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import feedbackSerializer
from .models import feedback
# Create your views here.

class test(APIView):
    def get(self,request):
        # return render(request,"index.html")
        sgs=feedback.objects.all()
        serializer=feedbackSerializer(sgs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=feedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)