from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse(Question.objects.order_by("-pub_date"))

def detail(request, question_id):
    return HttpResponse("투표 화면입니다.")

def results(request, question_id):
    return HttpResponse("투표 결과 화면입니다.")
