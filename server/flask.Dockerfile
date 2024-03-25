# Use the official Python image as base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /server

# Copy the server files to the working directory
COPY . /server
# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Flask server
CMD ["python", "server.py"]
