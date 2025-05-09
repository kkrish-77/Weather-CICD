# Weather App with Flask and Kubernetes

A simple weather application built with Flask, containerized with Docker, and deployed on Kubernetes using Minikube.

## Prerequisites

- Python 3.9+
- Docker
- Minikube
- kubectl
- OpenWeatherMap API key

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd weather-app
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up your OpenWeatherMap API key:
```bash
export WEATHER_API_KEY='your-api-key-here'
```

## Local Development

Run the application locally:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Docker Build

Build the Docker image:
```bash
docker build -t weather-app .
```

Run the container:
```bash
docker run -p 5000:5000 -e WEATHER_API_KEY='your-api-key-here' weather-app
```

## Kubernetes Deployment

1. Start Minikube:
```bash
minikube start
```

2. Create the Kubernetes secret for the API key:
```bash
kubectl create secret generic weather-secret --from-literal=api-key='your-api-key-here'
```

3. Apply the Kubernetes configuration:
```bash
kubectl apply -f k8s/deployment.yaml
```

4. Get the service URL:
```bash
minikube service weather-app-service --url
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Builds the application
2. Runs tests
3. Creates a Docker image
4. Deploys to Minikube

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── k8s/              # Kubernetes configurations
│   └── deployment.yaml
├── templates/        # HTML templates
│   └── index.html
└── .github/workflows/ # CI/CD configuration
    └── ci-cd.yml
``` 