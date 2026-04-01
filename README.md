# Mon projet : pipeline-test
Projet réalisé dans le cadre de mes apprentissages en DevOps. L'objectif est de mettre en place un pipeline CI/CD complet avec GitHub Actions, Docker, une API FastAPI et un frontend React.
# C'est quoi ce projet ?
c'est une application web simple avec:
- un frontend en React
- un backend en FastAPI
- une base de données MySQL
- tout est containerisé avec Docker
- et il y a un pipeline CI/CD avec GitHub Actions qui lance automatiquement des scans de sécurité et déploie l'application.
# Technologie utilisées :
- React (react@19.2.4)
- FastAPI (Python 3.12.3)
- MySQL (Ver 8.0.45)
- Docker (version 29.3.0)
- Docker Compose (v5.1.0)

# Pipeline de sécurité :
- GitHub Actions
- Gitleaks v2 — détection de secrets
- Checkov 3.2.513 — sécurité des fichiers de configuration
- Conftest — validation de règles personnalisées
- SonarCloud — qualité du code
- Anchore Syft 1.42.3 — génération SBOM
- Cosign v3 — signature des images Docker
- Snyk — vulnérabilités des dépendances
- Trivy — scan des images Docker
- Nginx — reverse proxy pour le déploiement
# Structure de projet:
devsecops-react/

├── .github/

│   └── workflows/

│       ├── CI.yml              # Pipeline de tests et sécurité

│       └── CD.yml              # Pipeline de déploiement

├── backend/

│   ├── dockerfile

│   ├── requirements.txt

│   └── main.py

├── frontend/

│   ├── Dockerfile

│   ├── package.json

│   └── src/

├── policy/                     # Règles Conftest (Rego)

├── .checkov.yaml               # Configuration Checkov

├── .gitleaks.toml              # Configuration Gitleaks

├── sonar-project.properties    # Configuration SonarCloud

├── docker-compose.yml

├── .env.example

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

- CD : si le CI passe, il déploie automatiquement en intégrant outils de sécurité a chaque étapes de test.

# Les outils de sécurité dans le pipeline
Voici tous les outils que j'ai intégrés dans le pipeline CI, dans l'ordre où ils s'exécutent, avec comment les configurer si vous voulez reproduire ce projet.

- Gitleaks — Détection de secrets dans le code: Gitleaks vérifie que personne n'a accidentellement mis un mot de passe ou une clé API dans le code source.

Il suffit d'ajouter ce step dans le fichier CI.yml
> On peut aussi ajouter un fichier .gitleaks.toml à la racine pour personnaliser les règles.

- Checkov — Sécurité des fichiers Docker et de configuration: Checkov analyse les Dockerfiles et autres fichiers de configuration pour détecter des mauvaises pratiques de sécurité, par exemple un container qui tourne en root ou un port sensible ouvert.

Il faut créer un fichier .checkov.yaml à la racine du projet. ## configure Checkov pour savoir quels fichiers scanner et quelles règles de sécurité appliquer.

et ajouter ce step dans CI.yml

- Conftest — Règles de sécurité personnalisées: Conftest permet de valider les Dockerfiles contre des règles qu'on écrit soi-même en langage Rego. Par exemple : interdire l'image latest, obliger un HEALTHCHECK, etc.

Les règles se placent dans le dossier policy/ dans un fichier '.rego' . Ensuite on ajoute ce step dans CI.yml

- SonarQube — Qualité et sécurité du code: SonarCloud analyse le code source pour trouver des bugs, des vulnérabilités et du code mal écrit.

Il faut créer un compte sur sonarcloud.io (connexion avec GitHub ).

> Étapes de configuration :

1- Se connecter sur sonarcloud.io avec GitHub

2- Cliquer sur "+" → "Analyze new project" → sélectionner le repo → "Set up"

3- Choisir "Previous version" → "Create project"

4- Aller dans Administration → Analysis Method et désactiver l'Automatic Analysis (sinon conflit avec le pipeline)

5- Copier le token généré et l'ajouter dans GitHub Secrets sous le nom "SONAR_TOKEN"
>> Remarque: Le projet doit être créé manuellement sur SonarCloud avant le premier lancement du pipeline, sinon il échoue avec une erreur "project not found".

Créer le fichier sonar-project.properties à la racine ## c’est le fichier de configuration qui permet à SonarQube d’analyser correctement ton projet

Puis ajouter ce step dans CI.yml

- GitHub Container Registry (GHCR) — Stockage des images Docker: GHCR est un service gratuit intégré à GitHub pour stocker les images Docker. Pas besoin de Docker Hub.

Il faut ajouter packages: write dans les permissions du workflow, puis ces steps

>> Remarque: Les noms d'images GHCR doivent être en minuscules. J'utilise une variable OWNER avec tr '[:upper:]' '[:lower:]' pour convertir automatiquement, même si le nom d'utilisateur GitHub contient des majuscules.

- SBOM — Inventaire des composants: Le SBOM (Software Bill of Materials) est une liste complète de tous les composants utilisés dans l'application. C'est utile pour savoir rapidement si un composant vulnérable est présent.

Il suffit d'ajouter ce step dans le fichier CI.yml

- Cosign — Signature des images Docker: Cosign signe les images Docker pour prouver qu'elles n'ont pas été modifiées après leur création. C'est l'équivalent d'une signature numérique sur un document.

Il faut d'abord installer sur ta machine et aprés générer une paire de clés en local: cosign generate-key-pair

Cela crée deux fichiers : cosign.key (clé privée) et cosign.pub (clé publique). Il faut ajouter le contenu de cosign.key dans GitHub Secrets sous le nom "COSIGN_KEY".

Ensuit ajoute ce step dans CI.yml

- Snyk— Vulnérabilités des dépendances: Snyk vérifie si les bibliothèques utilisées dans le code ont des failles de sécurité connues.

Il faut créer un compte sur app.snyk.io (connexion avec GitHub).

> Étapes de configuration :

1- Se connecter sur app.snyk.io

2- Aller dans Account Settings → copier l'Auth Token

3- L'ajouter dans GitHub Secrets sous le nom "SNYK_TOKEN"

Ensuite ajoute ce step dans CI.yml

>> Remarque : Il faut toujours spécifier le chemin du fichier avec --file=, sinon Snyk cherche dans la racine du projet et ne trouve rien. Ajoutez aussi --skip-unresolved pour le backend Python si les dépendances ne sont pas installées dans le runner.

- Trivy — Scan des images Docker: Trivy scanne les images Docker et le code source pour trouver des vulnérabilités connues.

Il suffit d'ajouter ce step dans le fichier CI.yml

# Secrets GitHub à configurer:

- Tous les secrets se configurent dans : GitHub → votre repo → Settings → Secrets and variables → Actions → New repository secret

* SONAR_TOKEN : généré sur SonarCloud → Account Settings → Security → Generate Token

* SNYK_TOKEN : disponible sur app.snyk.io → Account Settings → Auth Token

* COSIGN_KEY : contenu du fichier cosign.key généré avec cosign generate-key-pair

* GITHUB_TOKEN : fourni automatiquement par GitHub Actions, rien à faire

# Lancement automatiques des pipelines (CI/CD):

- À chaque git push, le pipeline se déclenche automatiquement. Vous pouvez suivre l'exécution dans l'onglet Actions de votre repo GitHub.

> git push → CI (tests + build) → CD (déploiement automatique):
- connecter vscode avec github (optionnel)
- creation de repository sur GitHub (manuellement)

git  init

git add .                           #  sélectionne tous les fichiers modifiés pour les
préparer à être sauvegardés

git commit -m ""                    # sauvegarde les fichiers sélectionnés avec un message
qui décrit ce que tu as fait

git remote add origin https://github.com/Ghofranez/pipeline-test.git

git branch -M master

git branch                          # Vérifier le nom du branche

git push -u origin $nomdubranche    # envoie tes sauvegardes locales vers GitHub sur la branche choisie


# Infrastructure (Déploiment)
Pour le déploiement, j'utilise une machine virtuelle Ubuntu Server sur VirtualBox sur laquelle tourne à la fois le runner GitHub Actions (self-hosted) et le serveur Nginx.

Pourquoi un runner self-hosted ?
Ma VM est en local sur VirtualBox, donc GitHub ne peut pas y accéder directement. Le runner est installé sur la VM pour qu'il écoute GitHub et exécute le déploiement de mon côté.

> Voici toutes les étapes que j'ai suivies pour tout configurer :

1- Préparer la VM Ubuntu:Mettre à jour le système et installer les outils de base (curl, git)

2- Installer Docker sur la VM et vérifier que Docker fonctionne:

Docker est nécessaire pour lancer les containers de l'application sur le serveur

3- Configurer le runnerself-hosted GitHub Actions et lancer le runner en tant que service:

Le runner self-hosted permet à GitHub Actions de lancer le déploiement directement sur ma VM au lieu des serveurs de GitHub.

> J'ai utilisé un runner self-hosted parce que ma VM est en local sur VirtualBox, donc GitHub ne peut pas y accéder directement. Le runner est installé sur la VM pour qu'il écoute GitHub et exécute le déploiement de mon côté.

4- Installer et configurer Nginx:

Nginx comme reverse proxy : il reçoit les requêtes et les redirige vers le bon service (React sur le port 3000 ou FastAPI sur le port 8000).
