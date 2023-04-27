from django.urls import path
from .views import UCL21_22, club_joueurs, joueur_stats, stats_detail

urlpatterns = [
    path('', UCL21_22, name="UCL21_22"),
    path('club_joueurs/', club_joueurs, name='club_joueurs'),
    path('joueur_stats/', joueur_stats, name='joueur_stats'),  
    path('stats_detail/', stats_detail, name='stats_detail')
]