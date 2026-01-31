# Gestionnaire de dépenses en ligne de commande

Outil en ligne de commande permettant d’enregistrer des revenus et des dépenses, de les catégoriser et de suivre l’évolution du solde dans le temps.
⚠️ Ce projet est personnel et ne remplace pas un gestionnaire de mots de passe professionnel.

## Fonctionnalités

### 1 — Initialisation du fichier de dépenses
- Création automatique du fichier `depenses.csv` au premier lancement
- `csv`: Écriture de l’en-tête CSV : `date`, `somme`, `intitule`, `categorie`, `balance`
- `os`: Vérification de l’existence du fichier

### 2 — Lecture et parsing des dépenses
- `csv.DictReader`: Lecture complète du fichier CSV existant
- Conversion des montants et soldes en valeurs numériques (`float`)
- Stockage des dépenses sous forme de dictionnaires Python


### 3 — Ajout d’une dépense ou d’un revenu
- Saisie interactive via la ligne de commande : `montant` (positif ou négatif), `intitulé`, `catégorie`
- `datetime`: Génération automatique de la date et de l’heure
- `csv.DictWriter` : réécriture complète du fichier CSV

### 4 — Calcul et suivi du solde (balance)
- Calcul cumulatif du solde après chaque opération
- Stockage du solde dans chaque ligne du fichier CSV

### 5 — Consultation de l’historique des dépenses
- Affiche les dépenses dans le terminal avec `date`, `montant`, `intitulé`, `catégorie`, `solde` (après l'opération)
