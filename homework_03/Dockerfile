# How to build this docker image:
# docker build -t mypythonapp .
#
# How to run this container:
# docker run -p 8000:8000 mypythonapp

# Use an official Python runtime as a parent image
FROM python:3.9-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add metadata to an image to describe how to run a container based on this image
LABEL org.opencontainers.image.source https://github.com/LavrenovDanila/python_homework/tree/main/homework_03

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]