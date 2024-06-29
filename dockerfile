#Docker File
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install system dependencies including snapd
RUN apt-get update && apt-get install -y curl \
    build-essential \
    libpq-dev \
    snapd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -U -r requirements.txt

# Install ollama using snap
RUN curl -fsSL https://ollama.com/install.sh | sh
# Download the model to the local (adjust as per your requirements)
RUN ollama pull mistral

# Run the model (adjust as per your requirements)
CMD ["ollama", "serve"]

# Copy the rest of the application code
COPY . /code/

# Run migrations and collect static files (if needed)
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Expose the port that the development server uses
EXPOSE 8000

# Define the command to run your Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
