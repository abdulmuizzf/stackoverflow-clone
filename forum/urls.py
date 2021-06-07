from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'forum'

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename='questions')
urlpatterns = router.urls
