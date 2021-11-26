import graphene
from graphene_django import DjangoObjectType

from .models import Question, Choice


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']


class ChoicesType(DjangoObjectType):
    class Meta:
        model = Choice
        exclude = ['question', 'choice_text', 'votes']


class Query(graphene.ObjectType):
    question = graphene.List(QuestionType)
    choice = graphene.List(ChoicesType)

    def resolve_question(self, info, **kwargs):
        return Question.objects.all()

    def resolve_choice(self, info, **kwargs):
        return Choice.objects.all()


schema = graphene.Schema(query=Query)
