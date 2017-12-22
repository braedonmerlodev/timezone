from django.shortcuts import render, HttpResponse, redirect
from time import strftime
def index(request):
  context = {
  "time": strftime("%Y-%m-%d %I:%M %p")
  }
  return render(request,'time_app/index.html', context)