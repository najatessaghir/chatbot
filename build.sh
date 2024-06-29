pip install -r -U requirements.txt

snap install ollama 
ollama pull mistral 
ollama serve 

python manage.py migrate 

