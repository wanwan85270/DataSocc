from django.urls import path
from .views import UCL21_22, joueur_detail, joueur

urlpatterns = [
    path('', UCL21_22, name="UCL21_22"),
    path('joueurs_detail/', joueur_detail, name='joueur_detail'),
    path('joueur/<int:joueur_id>/', joueur, name='joueur'),
]