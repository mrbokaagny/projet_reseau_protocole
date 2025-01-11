# Projet Réseau et Protocole

Ce projet a pour objectif de comparer les performances des protocoles HTTP (1.1, 2.0, et 3.0) à travers un client Python qui mesure les temps de téléchargement et génère des graphiques pour visualiser les résultats.

## Prérequis

Avant de démarrer le projet, assurez-vous d'avoir installé :

- **Python 3.10+** (compatible avec HTTP/3 et Matplotlib)
- **Pip** (gestionnaire de paquets Python)

## Installation

Clonez le dépôt du projet :

```bash
git clone https://github.com/mrbokaagny/projet_reseau_protocole.git
```

Accédez au répertoire du projet :

```bash
cd projet_reseau_protocole
```

Créez un environnement virtuel pour isoler les dépendances :

```bash
python -m venv .venv
```

Activez l'environnement virtuel :

- **Windows** :
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/Mac** :
  ```bash
  source .venv/bin/activate
  ```

Installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

## Démarrage du projet

1. Assurez-vous que votre environnement virtuel est activé.
2. Exécutez le fichier principal :

```bash
python main.py
```

Ce script effectuera les tests de téléchargement avec les versions HTTP spécifiées et générera un graphique comparatif des performances.

## Résolution des problèmes

### Erreur liée à Tcl/Tk
Si vous rencontrez des erreurs liées à Tcl/Tk (exemple : `_tkinter.TclError`), suivez ces étapes :

1. Réinstallez Python en activant l'option **Tcl/Tk**.
2. Installez Tcl/Tk séparément via [ActiveState Tcl](https://www.activestate.com/products/tcl/).
3. Ajoutez les chemins Tcl/Tk à votre variable d'environnement `PATH` si nécessaire.


## Structure du projet

- **`main.py`** : Point d'entrée principal du projet.
- **`core.py`** : Contient la classe principale pour la gestion des graphiques et les tests.
- **`requirements.txt`** : Liste des dépendances nécessaires.

## Contribution

1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b ma-branche
   ```
3. Effectuez vos modifications et validez-les :
   ```bash
   git commit -m "Description des modifications"
   ```
4. Poussez vos modifications :
   ```bash
   git push origin ma-branche
   ```
5. Ouvrez une Pull Request sur le dépôt principal.
