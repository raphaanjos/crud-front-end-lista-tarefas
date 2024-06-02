from django.shortcuts import render
from django.http import HttpResponse


def applist_list(request):
    nome = "Raphael"
    alunos = ["Raphael", "Raquel", "Wagner", "Dayse"]
    return render(
        request, "applist/applist_list.html", {"nome": nome, "alunos": alunos}
    )
