# FactureCloud

## Vue d'ensemble

FactureCloud est une application de facturation destinée aux PME camerounaises. Elle sert de support unique à tous les travaux pratiques de la matière TVL (Tests & Validation de Logiciel) en MASTER 2 SIGL. Chaque TP ajoute une couche de test au même système et les étudiants construisent progressivement un dossier de test qui grossit de séance en séance.

## Architecture du système

FactureCloud est structuré en trois services App Engine, une base de données et un fournisseur d'envoi externe.

- api-factures : point d'entrée principal des clients
- service-calcul : calcul des montants, TVA et pénalités
- service-notifications : gestion des relances et notifications
- Base de données : stocke les factures, les paiements et les états
- Fournisseur d'envoi : simulé par un bouchon pendant les tests

Les clients n'appellent que api-factures, qui s'appuie sur service-calcul pour les montants et sur service-notifications pour les relances.

## Règles métier à tester

Les règles métier couvertes par le projet sont les suivantes :

- R1 : une facture contient de 1 à 50 lignes ; quantité entière ≥ 1 ; prix unitaire HT entier ≥ 1.
- R2 : statuts de facture (BROUILLON, EMISE, PARTIELLEMENT_PAYEE, PAYEE, ANNULEE) ; l'annulation n'est possible que depuis BROUILLON ou EMISE.
- R3 : une facture émise n'est plus modifiable ; le numéro est unique et séquentiel (format FC-AAAA-NNNNNN).
- R4 : paiement par espèces, virement ou mobile money ; un paiement ne dépasse pas le reste dû.
- R5 : TVA = 19,25 % du montant HT (paramétrable), arrondie au franc le plus proche.
- R6 : pénalité de retard = 1,5 % du reste dû TTC par mois entamé après l'échéance, plafonnée à 10 % du TTC.
- R7 : échéance par défaut = émission + 30 jours, ou + 60 jours pour un client de catégorie ADMINISTRATION.
- R8 : notification (SMS ou courriel) à l'émission, 5 jours avant l'échéance et à chaque relance ; 3 relances maximum ; 2 nouvelles tentatives en cas d'échec ; puis statut ECHEC.
- R9 : chaque route exige un jeton ; rôle COMPTABLE = lecture et écriture ; rôle LECTEUR = lecture seule.

## Environnement technique

- Langage : Python 3, Flask
- Services : trois services App Engine
- Stockage : Datastore, émulateur local en TP
- Données : fichiers CSV fictifs
- Tests : pytest, coverage.py, mutmut, Postman/Newman, Locust
- Analyse statique et sécurité : pylint, bandit, SonarQube, OWASP ZAP
- Intégration continue : GitHub Actions (introduit au TP9)
- Suivi des anomalies : GitHub Issues

## Organisation du dépôt

Le dépôt est organisé autour de l'application et des livrables de tests :

- api-factures : service API principal
- service-calcul : logique de calcul et règles métier
- service-notifications : générateur de notifications et relances
- tests : suites de tests, rapports et fichiers de validation
- docs : documentation et rapports du projet
- data : jeux de données utilisés par les services

## Objectif final

Le but du projet n'est pas seulement de tester une application, mais de construire un vrai dossier de validation de logiciel, à travers une démarche structurée, reproductible et argumentée, en vue d'une décision de mise en production.

---

Ce README sert de référence de contexte pour le projet. Il doit évoluer au fil des livrables et des étapes de validation.