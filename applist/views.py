from django.shortcuts import render
from .models import AppList


def applist_list(request):
    list = AppList.objects.all()

    return render(request, "applist/applist_list.html", {"list": list})
