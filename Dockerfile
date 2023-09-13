# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose port 8080 for your FastAPI application
EXPOSE 8080

# Start the FastAPI application on port 8080
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
