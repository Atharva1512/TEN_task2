from rest_framework import serializers
from feedback.models import feedback
from django import forms
class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        # fields=['name','date','suggestion','rating']
        fields='__all__'

        