from django.db import models

# Create your models here.

class modelUCL(models.Model):
    nom_joueur = models.CharField(max_length=75)
    club = models.CharField(max_length=75)
    position = models.CharField(max_length=30)
    minutes_jouées = models.FloatField(default=0.0)
    match_joués = models.FloatField(default=0.0)
    buts = models.FloatField(default=0.0)
    passes_décisives = models.FloatField(default=0.0)
    distance_parcourue_km = models.FloatField(default=0.0)
    corner_tiré = models.FloatField(default=0.0)
    hors_jeu = models.FloatField(default=0.0)
    dribbles = models.FloatField(default=0.0)
    total_tir = models.FloatField(default=0.0)
    tir_cadré = models.FloatField(default=0.0)
    tir_non_cadré = models.FloatField(default=0.0)
    tir_bloqué = models.FloatField(default=0.0)
    ballons_récupérés = models.FloatField(default=0.0)
    tacles = models.FloatField(default=0.0)
    tacles_réussi = models.FloatField(default=0.0)
    tacles_loupé = models.FloatField(default=0.0)
    joueur_éliminé = models.FloatField(default=0.0)
    fautes_commmies = models.FloatField(default=0.0)
    fautes_subies = models.FloatField(default=0.0)
    carton_jaune = models.FloatField(default=0.0)
    carton_rouge = models.FloatField(default=0.0)
    pourcent_passes_réussies = models.FloatField(default=0.0)
    passes_tentées = models.FloatField(default=0.0)
    passes_réussies = models.FloatField(default=0.0)
    pourcent_transversales_réussies = models.FloatField(default=0.0)
    transversales_tentées = models.FloatField(default=0.0)
    transversales_réussies = models.FloatField(default=0.0)
    coup_franc_tirés = models.FloatField(default=0.0)
    tirs_sauvés = models.FloatField(default=0.0)
    buts_concédés = models.FloatField(default=0.0)
    penalty_sauvé = models.FloatField(default=0.0)
    cleansheets = models.FloatField(default=0.0)
    but_du_pied_droit = models.FloatField(default=0.0)
    but_du_pied_gauche = models.FloatField(default=0.0)
    but_de_la_tête = models.FloatField(default=0.0)
    but_autres_façons = models.FloatField(default=0.0)
    but_intérieur_surface = models.FloatField(default=0.0)
    but_dehors_surface = models.FloatField(default=0.0)
    penaltys = models.FloatField(default=0.0)

    def __str__(self):
        return self.nom_joueur