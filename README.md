# Gestionnaire de dépenses en ligne de commande

Outil en ligne de commande permettant d’enregistrer des revenus et des dépenses, de les catégoriser et de suivre l’évolution du solde dans le temps.

⚠️ Ce projet est personnel et ne remplace pas un gestionnaire de dépenses professionnel.

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

## Installation et utilisation

### Prérequis
- Python 3.8 ou plus récent
- Un terminal (Linux, macOS ou Windows)

### Installation
1. Cloner le dépôt :
```bash
git clone https://github.com/Roland-Ung/Projet_Gestionnaire_de_depenses.git
cd Projet_Gestionnaire_de_depenses
```

2. Créer un environnement virtuel (optionnel)
```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

### Utilisation

**Lancer le programme**
```bash
python main.py
```
Le fichier `dépenses.csv` sera crée automatiquement au premier lancement



**Menu principal**

Une fois le programme lancé, un menu intéractif s'affiche dans le terminal
1. Ajouter une dépense
2. Lister les dépenses
3. Quitter

L’utilisateur doit saisir le numéro correspondant à l’action souhaitée



**Ajouter une dépense**
1. Lancer le programme
2. Choisir l’option `1` dans le menu  
3. Renseigner :
   - le montant (négatif pour une dépense, positif pour un revenu)
   - l’intitulé
   - la catégorie



**Lister les dépenses**
1. Lancer le programme
2. Choisir l’option `2` dans le menu



**Quitter le programme**

Choisir l’option `3` dans le menu


## Structure du projet

```
Projet_Gestionnaire_de_depenses/
│
├── main.py              Programme contenant chaque fonction et le 'main'
├── depenses.csv         Fichier où sont enregistrées les dépenses
├── .gitignore           Fichiers à exclure de Git (venv, password_store...)
├── requirements.txt     Liste des dépendances Python
└── README.md
```
