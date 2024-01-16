def tester_pourcentage_superieur_50(us_a, us_b, us_c, us_d):
    us_sup_50 = [] 

    if us_a >= 50:
        us_sup_50.append("US A")
    if us_b >= 50:
        us_sup_50.append("US B")
    if us_c >= 50:
        us_sup_50.append("US C")
    if us_d >= 50:
        us_sup_50.append("US D")

    return us_sup_50

def tester_pourcentage(pourcentage):
    if pourcentage >= 50:
        return "le travail avancé"
    else:
        return "fait attention"

###################################################################
print("L’application qui réalise vos souhaits")
Jour= int(input("Entre le jour : "))
mois = input("Entre le mois: ")
# Afficher les valeurs entrées par l'utilisateur
print("Le jour est :", Jour)
print("Le mois est:", mois)
print("******************************************************************")

if mois.lower() == "janvier" :
    print("[EPIC] perdre du poids")
    print("[US A] manger equilibré")
    print("[US B] faire du sport")
    print("[US C] Respecter les heures de sommeil")
    print("[US D] respect les heures de repas")
    
    A = int(input("entrez le pourcentage de l'US A : "))
    B = int(input("entrez le pourcentage de l'US B : "))
    C = int(input("entrez le pourcentage de l'US C : "))
    D = int(input("entrez le pourcentage de l'US D : "))
    resultats = tester_pourcentage_superieur_50(A, B, C,D)
    if resultats:
        print("Les US suivant sont avancés : ", ', '.join(resultats))
    else:
        print("US retarder")

elif mois.lower() == "février":
    print("[EPIC] Apprentissage d'une nouvelle compétence")
    print("[US A] Allouer du temps quotidien à l'apprentissage")
    print("[US B] Participer à des cours en ligne")
    print("[US C] Rejoindre des groupes d'étude")

elif mois.lower() == "mars":
    print("[EPIC] Amélioration de la forme physique")
    print("[US A] Suivre un programme d'entraînement régulier")
    print("[US B] Suivre un régime alimentaire équilibré")
    print("[US C] Participer à des activités sportives locales")