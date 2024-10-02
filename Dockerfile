# Base image with Python
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies for image processing
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install tensorflow==2.15.0 keras==2.15.0 keras-cv==0.6.0 tensorflow-datasets==4.9.6 keras-core==0.1.7 \
                streamlit matplotlib pillow

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]

