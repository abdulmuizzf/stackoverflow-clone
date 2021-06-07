from rest_framework import serializers

from .models import Question, Answer, QuestionComment, AnswerComment

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = ['body', 'author', 'votes', 'timestamp']

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'author', 'tags', 'votes', 'views', 'timestamp']

class QuestionSummarySerializer(QuestionSerializer):
    answer_count = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'title','author', 'tags', 'votes', 'answer_count', 'views', 'timestamp']

    def get_answer_count(self, question):
        return question.answer_set.count()

class QuestionDisplaySerializer(QuestionSerializer):
    answer_set = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'author', 'tags', 'votes', 'answer_set', 'views', 'timestamp']


