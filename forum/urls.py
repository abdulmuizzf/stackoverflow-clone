from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)