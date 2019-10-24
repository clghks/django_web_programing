from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("투표 목록 화면입니다.")

def detail(request, question_id):
    return HttpResponse("투표 화면입니다.")

def results(request, question_id):
    return HttpResponse("투표 결과 화면입니다.")
