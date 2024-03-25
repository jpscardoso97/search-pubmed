# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /server

# Copy the current directory contents into the container at /app
COPY . /server

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run Celery worker when the container launches
CMD ["celery", "-A", "background_svc", "worker", "--loglevel=info", "--uid=nobody"]