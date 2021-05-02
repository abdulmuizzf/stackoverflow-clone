from django.shortcuts import render
from django.views import generic

from .models import Question

class IndexView(generic.ListView):
    template_name = "forum/index.html"

    def get_queryset(self):
        """ Return top 15 questions """
        return Question.objects.order_by('-timestamp')[:15]

class DetailView(generic.DetailView):
    model = Question
    template_name = "forum/detail.html"
