# Use the official Python image from the DockerHub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask, SQLite, and other necessary packages
RUN pip install flask flask-cors

# Expose port 5000 to the outside world
EXPOSE 5000

# Define the environment variable to make Flask discover the app
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
