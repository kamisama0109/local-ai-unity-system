# Dockerfile for Qwen LLM GPU Container

FROM nvidia/cuda:11.4.2-cudnn8-runtime-ubuntu20.04

# Set the working directory
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the necessary port (example: 8080)
EXPOSE 8080

# Command to run the application
CMD ["python3", "your_application.py"]
