

# CI/CD Flask Application

This project demonstrates how to set up a Flask web application with a CI/CD pipeline using Docker, GitHub Actions, and Docker Hub.

Overview:
Welcome to CI/CD for Flask App, a comprehensive solution designed to establish a robust Continuous Integration and Continuous Deployment (CI/CD) pipeline for deploying Flask applications. This project's primary objective is to automate the deployment process, ensuring that changes to your Flask application are built, tested, and deployed seamlessly.

Purpose:
CI/CD for Flask App serves the purpose of simplifying the deployment process for Flask applications. It eliminates manual tasks, reducing the risk of human errors and accelerating the delivery of new features and bug fixes.

Accomplishments:
This CI/CD project streamlines the development workflow by integrating automated testing, building Docker containers, and orchestrating deployments. By doing so, it enhances the reliability and efficiency of your Flask application deployment, making it well-suited for both development and production environments.



## Project Structure

 structure of project and role of each directory and important files.

/project-root
│
├── app.py            # The main Flask application
├── .github/workflows # GitHub Actions workflows
│
├── .Tests            # Directory for unit tests
│   └── test_app.py   # Test cases for the Flask app
│
├── Dockerfile        # Instructions for building a Docker image
├── requirements.txt  # List of Python dependencies
│
└── README.md         # This README file

## Getting Started

instructions for setting up the project locally, including prerequisites and installation steps.

### Prerequisites

Include versions if relevant.

- [Docker](https://www.docker.com/)
- [Python 3.9](https://www.python.org/)

### Installation

Step-by-step instructions to get your project running locally:

1. Clone the repository:

   
   git clone https://github.com/Malatesh-Patil-67/cicd-flask-app.git
   cd cicd-flask-app


Usage
GitHub Repository Setup:

Begin by creating a GitHub repository for your Flask application.
Clone your GitHub repository to your local development environment.

Docker Configuration:
Ensure that you have Docker installed on your local machine.
Add a Dockerfile to your Flask project's root directory for containerization.

GitHub Actions Workflow:
Create a GitHub Actions workflow to automate your CI/CD pipeline.
Use the provided .github/workflows/main.yml file as a template for your workflow.

GitHub Secrets:
Go to your GitHub repository's "Settings" > "Secrets" and add the following secrets:
DOCKERHUB_USERNAME: Your Docker Hub username.
DOCKERHUB_PASSWORD: Your Docker Hub password or access token.

GitHub Push:
Push your code changes to your GitHub repository. Ensure you push to the main branch.

CI/CD Pipeline:
GitHub Actions will automatically build and test your Flask application using the Docker image defined in the Dockerfile.

Docker Hub:
After a successful build, the Docker image is pushed to Docker Hub.

Deployment:
On the production server, ensure you have Docker installed.

Pull the Docker image using the command:
docker pull your-docker-image-name:latest

Run the Flask application in a Docker container:
docker run -d -p 80:80 --name your-container-name your-docker-image-name:latest

Access Your App:
Your Flask application is now accessible at http://your-server-ip:80.
