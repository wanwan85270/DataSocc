from django.urls import path
from .views import UCL21_22, club_joueurs, club_joueurs_B, joueur_stats, joueur_stats_B, stats_detail, stats_detail_B, stats_detail_S

urlpatterns = [
    path('', UCL21_22, name="UCL21_22"),
    path('club_joueurs/', club_joueurs, name='club_joueurs'),
    path('club_joueurs_B/', club_joueurs_B, name='club_joueurs_B'),
    path('joueur_stats/', joueur_stats, name='joueur_stats'),
    path('joueur_stats_B/', joueur_stats_B, name='joueur_stats_B'),  
    path('stats_detail/', stats_detail, name='stats_detail'),
    path('stats_detail_B/', stats_detail_B, name='stats_detail_B'),
    path('stats_detail_S/', stats_detail_S, name='stats_detail_S')
]