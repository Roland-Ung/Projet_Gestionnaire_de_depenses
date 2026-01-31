import csv
import os
from datetime import datetime

FILENAME = "depenses.csv"


# ─────────────────────────────────────────────
# Initialisation du fichier CSV
# ─────────────────────────────────────────────
def init_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "somme", "intitule", "categorie", "balance"])


# ─────────────────────────────────────────────
# Lire toutes les dépenses
# ─────────────────────────────────────────────
def read_expenses():
    expenses = []
    if not os.path.exists(FILENAME):
        return expenses

    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f) #lit le fichier CSV en tant que dictionnaire
        for row in reader: #parcourt chaque ligne du CSV
            row["somme"] = float(row["somme"])
            row["balance"] = float(row["balance"])
            expenses.append(row) #ajoute la ligne à la liste des dépenses
    return expenses


# ─────────────────────────────────────────────
# Récupérer les catégories existantes
# ─────────────────────────────────────────────
def get_categories(expenses):
    return sorted(set(e["categorie"] for e in expenses))


# ─────────────────────────────────────────────
# Ajouter une dépense
# ─────────────────────────────────────────────
def add_expense():
    expenses = read_expenses() #récupère les dépenses existantes pour le calcul du solde

    somme = float(input("Montant (négatif autorisé) : "))
    intitule = input("Intitulé : ")
    categorie = input("Catégorie : ")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #-1 pour accéder au dernier élément de la liste
    previous_balance = expenses[-1]["balance"] if expenses else 0
    new_balance = previous_balance + somme

    expenses.append({
        "date": date,
        "somme": somme,
        "intitule": intitule,
        "categorie": categorie,
        "balance": new_balance
    })

    # Réécriture complète du CSV
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["date", "somme", "intitule", "categorie", "balance"]
        )
        writer.writeheader() #écrit l'en-tête
        writer.writerows(expenses) #écrit toutes les dépenses

    print("✓ Dépense enregistrée")


# ─────────────────────────────────────────────
# Afficher toutes les dépenses
# ─────────────────────────────────────────────
def list_expenses():
    expenses = read_expenses()
    for e in expenses:
        print(
            f"{e['date']} | {e['somme']:>8.2f} € | "
            f"{e['categorie']:<10} | {e['intitule']} | "
            f"Balance: {e['balance']:.2f} €"
        )


# ─────────────────────────────────────────────
# Menu principal
# ─────────────────────────────────────────────
def main():
    init_csv()

    while True:
        print("\n1. Ajouter une dépense")
        print("2. Lister les dépenses")
        print("3. Quitter")

        choice = input("Choix : ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            break
        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()
