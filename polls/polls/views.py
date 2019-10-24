from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    output = ""

    for q in Question.objects.order_by("-pub_date"):
        output += '<a href="/polls/' + str(q.id) + '">' + q.question_text + '</a><br>'

    return HttpResponse(output)

def detail(request, question_id):
   question = Question.objects.get(pk=question_id)
   output = question.question_text + " 투표 상세 화면입니다."

   return HttpResponse(output)

def results(request, question_id):
    return HttpResponse("투표 결과 화면입니다.")
