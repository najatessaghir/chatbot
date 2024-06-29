pip install -r -U requirements.txt

curl -fsSL https://ollama.com/install.sh | sh

ollama pull mistral

ollama serve

python manage.py runserver
