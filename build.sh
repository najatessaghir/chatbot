pip install -r -U requirements.txt

curl -fsSL https://ollama.com/install.sh | sh

ollama serve

ollama pull mistral

python manage.py runserver
