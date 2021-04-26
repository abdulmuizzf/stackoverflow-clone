from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Question, Answer, QuestionComment, AnswerComment, Tag

admin.site.register(User, UserAdmin)

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
admin.site.register(Tag)
