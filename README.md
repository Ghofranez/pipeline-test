# Mon projet : pipeline-test
Projet réalisé dans le cadre de mes apprentissages en DevOps. L'objectif est de mettre en place un pipeline CI/CD complet avec GitHub Actions, Docker, une API FastAPI et un frontend React.
# C'est quoi ce projet ?
c'est une application web simple avec:
- un frontend en React
- un backend en FastAPI (Python)
- une base de données MySQL
- tout est containerisé avec Docker
- et il y a un pipeline CI/CD avec GitHub Actions qui lance les tests automatiquement et déploie.
# Technologie utilisées :
- React
- FastAPI
- MySQL
- Docker / Docker Compose
- GitHub Actions
# Structure de projet:
pipeline-test/

├── .github/

│   └── workflows/       # les fichiers CI/CD

├── backend/             # API FastAPI + Python

├── frontend/            # Application React

├── docker-compose.yml   # Orchestre des services

├── .env.example         # Remplace par .env

└── README.md

# Comment lancer le projet
1- Cloner le repo:
- git clone https://github.com/Ghofranez/pipeline-test.git
- cd pipeline-test
2- Créer le fichier .env
- Le fichier .env doit contenir :
MYSQL_ROOT_PASSWORD=rootpassword

MYSQL_USER=user

MYSQL_PASSWORD=userpassword

MYSQL_DATABASE=mydb

BACKEND_DB_HOST=db

BACKEND_DB_PORT=3306

BACKEND_DB_USER=user

BACKEND_DB_PASSWORD=userpassword

BACKEND_DB_NAME=mydb

## Pour test local il faut installer docker et lancer manuellement:
3- Installer Docker Desktop:Docker Desktop inclut Docker et Docker Compose
- Windows / Mac: https://docs.docker.com/desktop/setup/install/windows-install/
- Linux (Ubuntu) :

sudo apt update

sudo apt install docker.io docker-compose-plugin -y

sudo systemctl start docker

-> vérification de l'installation:

docker --version

docker compose version

4- Lancer avec Docker Compose:

docker compose up --build

5- Vérifier les port :

docker compose ps

- L'application sera disponible sur :

> Frontend      -> http://localhost:3000

> Backend (API) -> http://localhost:8000

6- Pour arreter :

docker compose down

# Pipeline CI/CD

J'ai configuré deux workflows GitHub Actions :

- CI : à chaque push, il installe les dépendances, lance les tests et build les images

Docker en intégrant outils de sécurité a chaque test .

- CD : si le CI passe, il déploie automatiquement en intégrant outils de sécurité a

chaque étapes de test.

# Lancement automatiques des pipelines (CI/CD):

- À chaque git push, le pipeline GitHub Actions s'occupe automatiquement de tout :

> git push → CI (tests + build) → CD (déploiement automatique):
- connecter vscode avec github
- Installer Github CLI :  sudo apt install gh
- Connecter a GitHub CLI aprés faire la création du repository et push le projet:

gh repo create $project --public --source=. --push # creation de repository sur GitHub

git  init

git add .                           #  sélectionne tous les fichiers modifiés pour les
préparer à être sauvegardés

git commit -m ""                    # sauvegarde les fichiers sélectionnés avec un message
qui décrit ce que tu as fait

git remote add origin https://github.com/Ghofranez/project-test.git

git branch                          # Vérifier le nom du branche

git push -u origin $nomdubranche    # envoie tes sauvegardes locales vers GitHub sur la branche choisie

# Infrastructure (Déploiment)
Pour le déploiement, j'utilise une machine virtuelle Ubuntu-server (VirtualBox) sur

laquelle tourne à la fois le runner GitHub Actions (self-hosted) et le serveur Nginx.

> Voici toutes les étapes que j'ai suivies pour tout configurer :

1- Préparer la VM Ubuntu:Mettre à jour le système et installer les outils de base (curl
git)

2- Installer Docker sur la VM et vérifier que Docker fonctionne: Docker est nécessaire pour lancer les containers de l'application sur le serveur

3- Configurer le runnerself-hosted GitHub Actions et lancer le runner en tant que service: Le runner self-hosted permet à GitHub Actions de lancer le déploiement directement sur ma VM au lieu des serveurs de GitHub.

> J'ai utilisé un runner self-hosted parce que ma VM est en local sur VirtualBox, donc GitHub ne peut pas y accéder directement. Le runner est installé sur la VM pour qu'il écoute GitHub et exécute le déploiement de mon côté.

4- Installer et configurer Nginx:Nginx sert de reverse proxy : il reçoit les requêtes et les redirige vers le bon service (React sur le port 3000 ou FastAPI sur le port 8000).
