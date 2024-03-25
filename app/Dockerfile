# Use the official Streamlit image as base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the app files to the working directory
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
