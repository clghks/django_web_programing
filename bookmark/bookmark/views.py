from django.shortcuts import render
from django.views.generic import ListView
from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark