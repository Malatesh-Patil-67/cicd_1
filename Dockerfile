# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install Flask
# Install testing dependencies
RUN pip install pytest

RUN pip install pylint
# Add other dependencies if needed


# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
