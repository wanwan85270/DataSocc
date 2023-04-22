from datetime import datetime
from django.shortcuts import render
import csv
from .models import modelUCL



def BDDUCL21_22(request):
    date = datetime.today()
    with open('UCL21_22/data/UCL.csv', 'r', encoding='utf-8') as f:     #On ouvre le fichier csv
        lecteur_data = csv.reader(f)        # On donne à la variable lecteur_data, le contenu des données
        skip_colonne = next(lecteur_data)       # Permet d'ignorer la première ligne du fichier csv (nom des colonnes)
        for joueur in lecteur_data:         #Pour chaque ligne correspondant à un joueur
            nom_joueur=joueur[0]
            if not modelUCL.objects.filter(nom_joueur=nom_joueur).exists(): #ESSENTIEL SINON CA VA RELIRE LE FICHIER CSV ET REMETTRE LE NOMBRE DE LIGNES
                ucl = modelUCL(                 #On créé un nouvel objet, utilisant la class modelUCL
                    nom_joueur=nom_joueur,       #Pour chaque joueur, on passe chaque stat en spécifiant leur placement dans le df
                    club = joueur[1],
                    position = joueur[2],
                    minutes_jouées = joueur[3],
                    match_joués = joueur[4],
                    buts = joueur[5],
                    passes_décisives = joueur[6],
                    distance_parcourue_km = joueur[7],
                    corner_tiré = joueur[8],
                    hors_jeu = joueur[9],
                    dribbles = joueur[10],
                    total_tir = joueur[11],
                    tir_cadré = joueur[12],
                    tir_non_cadré = joueur[13],
                    tir_bloqué = joueur[14],
                    ballons_récupérés = joueur[15],
                    tacles = joueur[16],
                    tacles_réussi = joueur[17],
                    tacles_loupé = joueur[18],
                    joueur_éliminé = joueur[19],
                    fautes_commmies = joueur[20],
                    fautes_subies = joueur[21],
                    carton_jaune = joueur[22],
                    carton_rouge = joueur[23],
                    pourcent_passes_réussies = joueur[24],
                    passes_tentées = joueur[25],
                    passes_réussies = joueur[26],
                    pourcent_transversales_réussies = joueur[27],
                    transversales_tentées = joueur[28],
                    transversales_réussies = joueur[29],
                    coup_franc_tirés = joueur[30],
                    tirs_sauvés = joueur[31],
                    buts_concédés = joueur[32],
                    penalty_sauvé = joueur[33],
                    cleansheets = joueur[34],
                    but_du_pied_droit = joueur[35],
                    but_du_pied_gauche = joueur[36],
                    but_de_la_tête = joueur[37],
                    but_autres_façons = joueur[38],
                    but_intérieur_surface = joueur[39],
                    but_dehors_surface = joueur[40],
                    penaltys = joueur[41],
                )
                ucl.save()          #Permet d'enregistrer les données dans la BdD
    return render(request, "UCL21_22.html", context={"date": date,});

def UCL21_22(request):
    date = datetime.today()
    return render(request, "UCL21_22.html", context={"date": date, });

def joueur_detail(request):
    joueurs = modelUCL.objects.all()
    context = {'joueurs': joueurs}
    return render(request, 'joueur_detail.html', context)

def joueur(request, joueur_id):
    joueur = modelUCL.objects.get(id=joueur_id)
    context = {'joueur': joueur}
    return render(request, 'joueur_detail.html', context)
