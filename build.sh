pip install  -U -r requirements.txt

sudo curl -fsSL https://ollama.com/install.sh | sh
sudo ollama pull mistral 
sudo ollama serve 

python manage.py migrate 

