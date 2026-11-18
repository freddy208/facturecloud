# TVL501 - S3 - Trois petites fonctions de FactureCloud a analyser.
# Consigne : ne modifiez PAS ce fichier. Vous lisez, vous executez, vous analysez.


def calculer_tva(montant_ht):
    """Calcule la TVA d'une facture.

    Regle : la TVA vaut 19,25 % du montant hors taxe (HT), arrondie au franc
    le plus proche. Quand le calcul tombe exactement a mi-chemin (par exemple
    38,5), on arrondit vers le haut (39).
    Les montants sont des entiers en FCFA.
    """
    tva = montant_ht * 19.25 / 100
    return round(tva)


def total_facture(lignes):
    """Calcule le total hors taxe d'une facture.

    Regle : le total est la somme de (quantite x prix unitaire) de TOUTES les
    lignes. Une ligne est un couple (quantite, prix_unitaire).
    Une facture sans ligne a un total de 0.
    """
    total = 0
    for quantite, prix_unitaire in lignes:
        total = total + quantite * prix_unitaire
        return total


def niveau_relance(jours_de_retard):
    """Donne le niveau de relance d'une facture impayee.

    Regle du client : niveau 1 au-dela de 7 jours de retard, niveau 2 au-dela
    de 15 jours, niveau 3 au-dela de 30 jours. Avant, niveau 0 (pas de relance).
    Exemple donne par le client : 15 jours de retard, c'est encore le niveau 1.
    """
    if jours_de_retard >= 30:
        return 3
    elif jours_de_retard >= 15:
        return 2
    elif jours_de_retard >= 7:
        return 1
    return 0
