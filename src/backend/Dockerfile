FROM langchain/langchain:latest

# Install the required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install the required packages
RUN pip3 install --upgrade pip

# Install the required packages
RUN pip3 install -r requirements.txt

# Copy the source code
COPY . /app

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]