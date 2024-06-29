# AI chatbot

This Django project allows you to use a local Ai model to process files and answer questions using ollama . 
## Features

**Authentication:** User authentication and authorization to secure the application.
- **Process PDF Files:**  process PDF files to extract information.
- **Local AI Models:** Utilize local AI models for processing and answering questions.
- **Chat Interface:** Interactive chat interface to communicate with the AI model.

## Prerequisites

- Python 3.x
- Required Python packages (`django`, `langchain`, `chromadb` , `python-dotenv`,`PyPDF`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/najatessaghir/chatbot.git
   cd chatbot
2. Install the requirements
   ```bash
   pip install -r requirements.txt
3. load static files
   ```bash
   python manage.py makemigrations 
   python manage.py migrate
4. run the server
   ```bash
   python manage.py runserver

   
