from django.shortcuts import render
from django.http import HttpResponse

from .models import Kysymys   # .models tai kysely.models


def indeksi(request):
    kysymyslista = Kysymys.objects.order_by("-julkaisupvm")[:2]
    context = {
        "kysymykset": kysymyslista,
    }
    return render(request, "kysely/indeksi.html", context)


def näytä(request, question_id):
    return HttpResponse(f"Katsot juuri kysymystä {question_id}.")


def tulokset(request, question_id):
    return HttpResponse(f"Katsot kysymyksen {question_id} tuloksia.")


def äänestä(request, question_id):
    return HttpResponse(f"Olet äänestämässä kysmykseen {question_id}.")
