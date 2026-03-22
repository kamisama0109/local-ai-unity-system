# Dockerfile for Phi-3 LLM CPU Container

# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "your_script.py"]