from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import ListItem
from django.views import generic
from .form import NameForm
from django.urls import reverse
# Create your views here.

class IndexView(generic.ListView):
    template_name = "testing/index.html"
    context_object_name = "latest_list_item"

    def get_queryset(self):
        return ListItem.objects.order_by('-votes')

def get_name(request):
    try:
        selected_choice = ListItem(title=request.POST['submission'], author = "anon")
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        print("Bad")
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("testing:index"))

def upvote(request):
        selected_choice = ListItem.objects.get(id=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("testing:index"))
