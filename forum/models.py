from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Tag(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    votes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    deleted = models.BooleanField(default=False)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    deleted = models.BooleanField(default=False)

class QuestionComment(models.Model):
    parent = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='q_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='q_authors')
    body = models.TextField()
    timestamp = models.DateTimeField()
    deleted = models.BooleanField(default=False)

class AnswerComment(models.Model):
    parent = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='a_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_authors')
    body = models.TextField()
    timestamp = models.DateTimeField()
    deleted = models.BooleanField(default=False)
