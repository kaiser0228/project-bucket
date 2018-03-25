from django.urls import path

from . import views

app_name = "testing"
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('validate/', views.get_name, name='valid'),
    path('vote/', views.upvote, name='vote'),
]
