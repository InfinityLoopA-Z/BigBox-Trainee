from rest_framework import serializers

from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = []


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        exclude = []
