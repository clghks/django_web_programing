from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question

# Create your views here.
def index(request):
    output = ""

    for q in Question.objects.order_by("-pub_date"):
        output += '<a href="/polls/' + str(q.id) + '">' + q.question_text + '</a><br>'

    return HttpResponse(output)

def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   choice_list = get_list_or_404(question.choice_set)

   output = "<h1>" + question.question_text + "</h1>"
   output += '<form action="/polls/' + str(question_id) + '/results" method="get">'
   for choice in choice_list:
       output += '<input type="radio" name="choice" value="' + str(choice.id) + '">' + choice.choice_text + '</input><br>'
   output += '<input type="submit" value="Vote">'
   output += '</form>'

   return HttpResponse(output)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_list = get_list_or_404(question.choice_set)

    output = "<h1>" + question.question_text + "</h1>"
    for choice in choice_list:
        output += choice.choice_text + " : " + str(choice.votes) + "<br>"

    return HttpResponse(output)

def vote(request, question_id):
   question = Question.objects.get(pk=question_id)
   selected_choice = question.choice_set.get(pk=request.POST['choice'])

   selected_choice.votes += 1
   selected_choice.save()

   return HttpResponseRedirect('results')