from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
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
   for choice in choice_list:
       output += choice.choice_text + "<br>"

   return HttpResponse(output)

def results(request, question_id):
    return HttpResponse("투표 결과 화면입니다.")
