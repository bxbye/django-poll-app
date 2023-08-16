from django.shortcuts import get_object_or_404, render # render send HttpResponse object to client
from django.http import Http404
# Create your views here.
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
def results(request, question_id):
    context = {"question_id": question_id}
    return render(request, "polls/results.html", context)
def vote(request, question_id):
    context = {"question_id": question_id}
    return render(request, "polls/vote.html", context)