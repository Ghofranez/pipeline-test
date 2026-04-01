# Présentation:
Ce dossier contient le backend du projet, développé avec FastAPI.
Pour garder un environnement propre et éviter les conflits entre différentes versions de bibliothèques Python, nous utilisons un environnement virtuel (venv).

# Structure du dossier backend:
backend/

│── main.py              → fichier principal FastAPI

│── requirements.txt     → dépendances Python

│── venv/                → environnement virtuel (ne pas committer)

│── __pycache__/         → fichiers générés automatiquement

# Prérequis backend:
- Python : version 3.10
- FastAPI : version
- pip : gestionnaire de paquets Python
- venv : environnement virtuel Python (pour isoler les dépendances)

# Création et activation d'un environnement virtuel :
- venv est un outil qui permet de créer un environnement Python isolé. Cela évite que les bibliothèques de ton projet entrent en conflit avec celles installées globalement sur ton système.

 > Sur Linux / macOS
python3 -m venv venv #creation du l'environnement virtuel avec venv

source venv/bin/activate #Activer l'environnement virtuel

> Sur Windows
python -m venv venv   #creation du l'environnement virtuel avec venv

venv\Scripts\activate #Activer l'environnement virtuel

# Installer les dépendances:
pip install -r requirements.txt # fichier requirements.txt contient les dépendances

# Exécuter FastAPI en local:
uvicorn main:app --reload
 - main : fichier Python principal contenant app = FastAPI()

- --reload : redémarrage automatique à chaque modification du code

# Accéder à l'API sur :
http://127.0.0.1:8000

