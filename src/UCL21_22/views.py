from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models import Max
import csv
from .models import modelUCL
from matplotlib import pyplot as plt
import math
import numpy as np



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
    clubs = modelUCL.objects.values_list("club", flat=True).distinct()
    context = {"date": date, "clubs": clubs, "clubs_B":clubs}
    template_name = "club_list.html"
    return render(request, template_name, context=context)
    

def club_joueurs(request):
    club = request.GET.get('club')
    print(club)
    joueurs = modelUCL.objects.filter(club=club)
    print(joueurs)
    context = {'joueurs': joueurs}
    template_name = "joueur_list.html"
    return render(request, template_name, context=context)

def club_joueurs_B(request):
    club_B = request.GET.get('club_B')
    print(club_B)
    joueurs_B = modelUCL.objects.filter(club=club_B)
    print(joueurs_B)
    context = {'joueurs_B': joueurs_B}
    template_name = "joueur_B_list.html"
    return render(request, template_name, context=context)

def joueur_stats(request):
    joueur_id = request.GET.get("joueur")
    joueur = get_object_or_404(modelUCL, pk=joueur_id)
    joueur_stats = modelUCL.objects.filter(id=joueur_id)
    print(joueur_id)
    print(joueur)
    print(joueur_stats)
    context = {"joueur": joueur, "joueur_stats": joueur_stats}
    template_name = "statistiques_list.html"
    return render(request, template_name, context=context)

def joueur_stats_B(request):
    joueur_id_B = request.GET.get("joueur_B")
    joueur_B = get_object_or_404(modelUCL, pk=joueur_id_B)
    joueur_stats_B = modelUCL.objects.filter(id=joueur_id_B)
    print(joueur_id_B)
    print(joueur_B)
    print(joueur_stats_B)
    context = {"joueur_B": joueur_B, "joueur_stats_B": joueur_stats_B}
    template_name = "statistiques_list_B.html"
    return render(request, template_name, context=context)

def stats_detail(request):
    #on défini les variables
    stats = request.GET.getlist('stats')
    joueur_id = request.GET.get('joueur_id')
    joueur = get_object_or_404(modelUCL, pk=joueur_id)
    joueur_stats = []
    for stat in stats:
        joueur_stats.append(getattr(joueur, stat))
    print(stats)
    print(joueur_id)
    print(joueur)
    print(joueur_stats)

    joueur_stats_dict = {}
    for i in range(len(stats)):
        joueur_stats_dict[stats[i]] = joueur_stats[i]
    print(joueur_stats_dict)

    stats_names = list(joueur_stats_dict.keys())
    stats_values = list(joueur_stats_dict.values())
    print(stats_names)
    print(stats_values)

    max_values = []
    for stat in stats:
        max_value = modelUCL.objects.aggregate(Max(stat))[stat + '__max']
        max_values.append(max_value)    
        print (max_values)

    normalized_stats_values = [val/max_val for val, max_val in zip(stats_values, max_values)]

    #Sur quels angles les statistiques s'affichent sur le diagramme
    angles = [n / float(len(stats_names)) * 2 * math.pi for n in range(len(stats_names))] 
    print(angles)

    #Initialise le diagramme
    ax = plt.subplot(111, polar=True)
    #Pour avoir la première stat au sommet
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    #Dessine un axe par stat et les étiquettes
    plt.xticks(angles, stats_names)
    ax.plot(angles, normalized_stats_values, linewidth=1, linestyle='solid')
    ax.fill(angles, normalized_stats_values, 'blue', alpha=0.1)

    plt.ylim(0, 1.0)
    plt.title(joueur.nom_joueur + " - " + joueur.club)
    plt.show()

    context = {'joueur': joueur, 'stats': stats, 'joueur_stats_dict': joueur_stats_dict}
    template_name = 'joueur_detail.html'

    return render(request, template_name, context=context)


def stats_detail_B(request):
    stats_B = request.GET.getlist('stats_B')
    joueur_id_B = request.GET.get('joueur_id_B')
    joueur_B = get_object_or_404(modelUCL, pk=joueur_id_B)
    joueur_stats_B = []
    for stat in stats_B:
        joueur_stats_B.append(getattr(joueur_B, stat))
    print (stats_B)
    print(joueur_id_B)
    print(joueur_B)
    print(joueur_stats_B)

    joueur_stats_dict_B = {}
    for i in range(len(stats_B)):
        joueur_stats_dict_B[stats_B[i]] = joueur_stats_B[i]
    print(joueur_stats_dict_B)

    stats_names_B = list(joueur_stats_dict_B.keys())
    stats_values_B = list(joueur_stats_dict_B.values())
    print(stats_names_B)
    print(stats_values_B)

    max_values_B = []
    for stat in stats_B:
        max_value_B = modelUCL.objects.aggregate(Max(stat))[stat + '__max']
        max_values_B.append(max_value_B)    
        print (max_values_B)

    normalized_stats_values_B = [val/max_val for val, max_val in zip(stats_values_B, max_values_B)]
    print(normalized_stats_values_B)

    angles_B = [n / float(len(stats_names_B)) * 2 * math.pi for n in range(len(stats_names_B))] 
    print(angles_B)

    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles_B, stats_names_B)
    ax.plot(angles_B, normalized_stats_values_B, 'red', linewidth=1, linestyle='solid')
    ax.fill(angles_B, normalized_stats_values_B, 'red', alpha=0.3)

    plt.ylim(0, 1.0)
    plt.title(joueur_B.nom_joueur + " - " + joueur_B.club)
    plt.show()

    context = {'joueur': joueur_B, 'stats': stats_B,'joueur_stats_dict_B': joueur_stats_dict_B}
    template_name = 'joueur_detail.html'

    return render(request, template_name, context=context)

def stats_detail_S(request):
    joueur_id_S = request.GET.get('joueur_id_S')
    joueur_S = get_object_or_404(modelUCL, pk=joueur_id_S)
    print(joueur_id_S)
    print(joueur_S)
    
    stats_B_S = request.GET.getlist('stats_B')
    print(stats_B_S)
    joueur_id_B_S = request.GET.get('joueur_id_B')
    joueur_B_S = get_object_or_404(modelUCL, pk=joueur_id_B_S)   
    print(joueur_B_S)
    print(joueur_id_B_S) 
    
    joueur_stats_S = []
    joueur_stats_B_S = []
    for stat in stats_B_S:
        joueur_stats_S.append(getattr(joueur_S, stat))
        joueur_stats_B_S.append(getattr(joueur_B_S, stat))
        
    joueur_stats_dict_S = {}
    joueur_stats_dict_B_S = {}
    for i in range(len(stats_B_S)):
        joueur_stats_dict_S[stats_B_S[i]] = joueur_stats_S[i]
        joueur_stats_dict_B_S[stats_B_S[i]] = joueur_stats_B_S[i]

    stats_names_S = list(joueur_stats_dict_S.keys())
    stats_values_S = list(joueur_stats_dict_S.values())
    stats_values_B_S = list(joueur_stats_dict_B_S.values())

    max_values_S = []
    max_values_B_S = []
    for stat in stats_B_S:
        max_value_S = modelUCL.objects.aggregate(Max(stat))[stat + '__max']
        max_value_B_S = max_value_S
        max_values_S.append(max_value_S)
        max_values_B_S.append(max_value_B_S)

    normalized_stats_values_S = [val/max_val for val, max_val in zip(stats_values_S, max_values_S)]
    normalized_stats_values_B_S = [val/max_val for val, max_val in zip(stats_values_B_S, max_values_B_S)]

    angles = [n / float(len(stats_names_S)) * 2 * math.pi for n in range(len(stats_names_S))] 

    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(math.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles, stats_names_S)

    ax.plot(angles, normalized_stats_values_S, linewidth=1, linestyle='solid', color='blue', label=joueur_S.nom_joueur)
    ax.fill(angles, normalized_stats_values_S, 'blue', alpha=0.1)
    ax.plot(angles, normalized_stats_values_B_S, 'red', linewidth=1, linestyle='solid', label=joueur_B_S.nom_joueur)
    ax.fill(angles, normalized_stats_values_B_S, 'red', alpha=0.3)

    plt.ylim(0, 1.0)
    plt.title(joueur_S.nom_joueur + " - " + joueur_S.club + " vs " + joueur_B_S.nom_joueur + " - " + joueur_B_S.club)
    plt.legend(loc='upper right')
    plt.show()


    context = {'joueur': joueur_S, 'stats': stats_B_S, 'joueur_stats_dict': joueur_stats_dict_S,
               'joueur_B': joueur_B_S, 'joueur_stats_dict_B': joueur_stats_dict_B_S}
    template_name = 'diagram.html'

    return render(request, template_name, context=context)





