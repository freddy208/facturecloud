## Tests des composants & tests d'intregration

## Membres du groupe
```
KEPTUKWA NGOUMYIM Freddy
TENE Marie-Yanne
```
```Date : 19 Novembre 2026```

## A. Les attendus

## Niveau composant

| Fonction | Entrée | Attendu | Source de l'attendu |
|:---|:---|---:|:---|
| `total_ht` | `[(2, 5000), (1, 3000)]` | 13 000 FCFA | Le total HT d'une facture est la somme de quantité × prix unitaire de chaque ligne. |
| `total_ht` | `[]` | 0 FCFA | Le total HT d'une facture est la somme de quantité × prix unitaire de chaque ligne. |
| `calculer_remise` | `(13000, True)` | 1 300 FCFA | La remise est de 10 % du total HT pour un client fidèle, 0 sinon. |
| `calculer_remise` | `(13000, False)` | 0 FCFA | La remise est de 10 % du total HT pour un client fidèle, 0 sinon. |
| `calculer_tva` | `200` | 39 FCFA | La TVA est de 19,25 % du montant HT après remise. Elle est arrondie à l'entier le plus proche, 0,5 arrondi vers le haut. |
| `calculer_tva` | `11700` | 2 252 FCFA | La TVA est de 19,25 % du montant HT après remise. Elle est arrondie à l'entier le plus proche, 0,5 arrondi vers le haut. |


## Niveau intégration

| Fonction | Entrée | Client fidèle | Client non fidèle |
|:---|:---|---:|---:|
| `creer_facture` | `([(2, 5000), (1, 3000)], client_fidele)` |  |  |
| HT | Calcul du total des lignes | 13 000 FCFA | 13 000 FCFA |
| Remise | 10 % si client fidèle, sinon 0 | 1 300 FCFA | 0 FCFA |
| Net | HT − remise | 11 700 FCFA | 13 000 FCFA |
| TVA | 19,25 % du net, arrondie au franc | 2 252 FCFA | 2 503 FCFA |
| TTC | Net + TVA | 13 952 FCFA | 15 503 FCFA |
