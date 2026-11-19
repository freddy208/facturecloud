"""FactureCloud - module de facturation (version fournie pour le TP S4).

Regles de gestion (fictives, sans lien avec la reglementation reelle) :
- Les montants sont des entiers en FCFA.
- Le total HT d'une facture est la somme de quantite x prix unitaire de chaque ligne.
- La remise est de 10 % du total HT pour un client fidele, 0 sinon.
  Elle est arrondie a l'entier le plus proche, 0,5 arrondi vers le haut.
- La TVA est de 19,25 % du montant HT apres remise.
  Elle est arrondie a l'entier le plus proche, 0,5 arrondi vers le haut.
- Le total TTC est le montant HT apres remise plus la TVA.
"""


def total_ht(lignes):
    """Somme de quantite x prix unitaire. Liste vide : 0."""
    total = 0
    for quantite, prix_unitaire in lignes:
        total = total + quantite * prix_unitaire
    return total


def calculer_remise(total, client_fidele):
    """10 % du total pour un client fidele, 0 sinon (arrondi 0,5 vers le haut)."""
    if not client_fidele:
        return 0
    return (total * 10 + 50) // 100


def calculer_tva(montant_ht):
    """19,25 % du montant HT, arrondi a l'entier le plus proche (0,5 vers le haut)."""
    return (montant_ht * 1925 + 5000) // 10000


def creer_facture(lignes, client_fidele):
    """Retourne un dictionnaire avec ht, remise, net, tva et ttc."""
    ht = total_ht(lignes)
    remise = calculer_remise(ht, client_fidele)
    net = ht - remise
    tva = calculer_tva(ht)
    return {"ht": ht, "remise": remise, "net": net, "tva": tva, "ttc": net + tva}
