from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'