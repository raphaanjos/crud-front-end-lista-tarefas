from django.shortcuts import render
from django.http import HttpResponse


def applist_list(request):
    return render(request, "applist/home.html")
