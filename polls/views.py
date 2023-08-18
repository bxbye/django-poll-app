from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render # render send HttpResponse object to client
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Question, Choice
from django.db.models import F
from django.views import generic # for using generic views
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """
        Return the last five published questions.
        """
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by("-pub_date")[:5]# filter pub_date less or equal to now(current) date and time.
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now()) # less then or equal to now.

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte = timezone.now()) # less then or equal to now.


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # KeyError: Raised when a mapping (dictionary) key is not found in the set of existing keys.
        # redisplay the question voting form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question, 
                "error_message": "You didn't select a choice."
            }
        )
    else:
        selected_choice.votes = F("votes") + 1 # F class uses for avoid race conditioning
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # You should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn’t specific to Django; it’s good web development practice in general.