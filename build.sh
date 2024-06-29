pip install -r -U requiements.txt

snap install ollama 
ollama pull mistral 
ollama serve 

python manage.py migrate 

