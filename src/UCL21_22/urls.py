from django.urls import path
from .views import UCL21_22, joueur_detail

urlpatterns = [
    path('', UCL21_22, name="UCL21_22"),
    path('joueur_detail/', joueur_detail, name="joueur_detail")
]