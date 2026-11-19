from facturation import total_ht, calculer_remise, calculer_tva, creer_facture


# Test 1 : total HT avec deux lignes
def test_total_ht_deux_lignes():
    assert total_ht([(2, 5000), (1, 3000)]) == 13000


# Test 2 : total HT avec une liste vide
def test_total_ht_liste_vide():
    assert total_ht([]) == 0


# Test 3 : remise de 10 % pour un client fidele
def test_calculer_remise_client_fidele():
    assert calculer_remise(13000, True) == 1300


# Test 4 : aucune remise pour un client non fidele
def test_calculer_remise_client_non_fidele():
    assert calculer_remise(13000, False) == 0


# Test 5 : TVA de 19,25 % sur 200 FCFA
def test_calculer_tva_200():
    assert calculer_tva(200) == 39


# Test 6 : TVA de 19,25 % sur 11 700 FCFA
def test_calculer_tva_11700():
    assert calculer_tva(11700) == 2252

# Test 7 : facture d'un client fidele
def test_facture_client_fidele():
    facture = creer_facture([(2, 5000), (1, 3000)], True)

    assert facture["net"] == 11700
    assert facture["tva"] == 2252
    assert facture["ttc"] == 13952


# Test 8 : facture d'un client non fidele
def test_facture_client_non_fidele():
    facture = creer_facture([(2, 5000), (1, 3000)], False)

    assert facture["net"] == 13000
    assert facture["tva"] == 2503
    assert facture["ttc"] == 15503