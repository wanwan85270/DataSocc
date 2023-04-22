from django.urls import path
from .views import UCL21_22

urlpatterns = [
    path('', UCL21_22, name="UCL21_22"),
    path('joueur_detail/', UCL21_22, name="joueur_detail")
]