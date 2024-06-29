# Chatbot AI

Ce projet Django vous permet d'utiliser un modèle d'IA local pour traiter des fichiers et répondre à des questions en utilisant Ollama.

## Fonctionnalités

- **Authentification :** Authentification et autorisation des utilisateurs pour sécuriser l'application.
- **Traitement des fichiers PDF :** Traitez les fichiers PDF pour extraire des informations.
- **Modèles d'IA locaux :** Utilisez des modèles d'IA locaux pour traiter et répondre aux questions.
- **Interface de chat :** Interface de chat interactive pour communiquer avec le modèle d'IA.

## Prérequis

- Python 3.x
- Packages Python requis (`django`, `langchain`, `chromadb`, `python-dotenv`, `PyPDF`)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/najatessaghir/chatbot.git
   cd chatbot
2. Installez les exigences :
   ```bash
   pip install -r -U requirements.txt
3. Chargez les fichiers statiques :
   ```bash
   python manage.py makemigrations 
   python manage.py migrate
4. Lancez le serveur :
   ```bash
   python manage.py runserver

## Utilisation
    1. Accédez à l'application à l'adresse http://127.0.0.1:8000 dans votre navigateur web.
    2. Inscrivez-vous ou connectez-vous à votre compte.
    3. Téléchargez des fichiers PDF pour les traiter et interagissez avec le modèle d'IA via l'interface de chat.
   
