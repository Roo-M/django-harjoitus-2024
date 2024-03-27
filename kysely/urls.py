from django.urls import path

from . import views

urlpatterns = [
    # esim: /kyselyt/
    path("", views.indeksi, name="indeksi"),
    # esim: /kyselyt/5/
    path("<int:question_id>/", views.näytä, name="näytä"),
    # esim: /kyselyt/5/results/
    path("<int:question_id>/results/", views.tulokset, name="tulokset"),
    # esim: /kyselyt/5/vote/
    path("<int:question_id>/vote/", views.äänestä, name="äänestä"),
]
