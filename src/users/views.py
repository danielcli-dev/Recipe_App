from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class UserListView(LoginRequiredMixin, ListView):
   model = User
   template_name = 'users/list.html'

class UserDetailView(LoginRequiredMixin, DetailView):
   model = User
   template_name = 'users/detail.html'