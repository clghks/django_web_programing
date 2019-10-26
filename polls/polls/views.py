from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, pk):
   question = Question.objects.get(pk=pk)
   selected_choice = question.choice_set.get(pk=request.POST['choice'])

   selected_choice.votes += 1
   selected_choice.save()

   return HttpResponseRedirect('results')