pip install  -U -r requirements.txt

curl -sSL https://install.ollama.com | sh
ollama pull mistral 
ollama serve 

python manage.py migrate 

