from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Question
from .serializers import QuestionSerializer, QuestionSummarySerializer, QuestionDisplaySerializer

class QuestionViewSet(viewsets.ViewSet):
    
    def list(self, request, format=None):
        questions = Question.objects.order_by('-timestamp')[:15]
        serializer = QuestionSummarySerializer(questions, many=True)
        return Response(serializer.data)
    
    def create(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk, format=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionDisplaySerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk, format=None, **kwargs):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        partial = kwargs['partial']
        serializer = QuestionSerializer(question, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        return self.update(request, pk=None, partial=True)

    def destroy(self, request, pk, format=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        question.delete = True
        return Response(status=status.HTTP_200_OK)
    
