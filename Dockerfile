# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=main.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
