# FASTAPI

This project is a fastapi application built using Python. It includes instructions for running and testing the application locally and deploying it on a Kubernetes cluster on your local machine.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Testing Locally](#testing-locally)
- [Setting Up Kubernetes Locally](#setting-up-kubernetes-locally)
- [Deploying to Kubernetes](#deploying-to-kubernetes)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://docs.docker.com/get-docker/) installed on your machine
- [Python](https://www.python.org/downloads/) 3.7+ installed
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) or another local Kubernetes clustering tool
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) command-line tool
- [Helm]

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/DarshAsawa/fastapi-github-actions.git
    cd fastapi-github-actions
    ```

2. **Create a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    python3 -m pip install -r requirements.txt
    ```

## Running Locally

1. **Start the application**:

    ```bash
    python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
    ```

2. **Access the application**:

   Open your web browser and go to `http://0.0.0.0:8080` (or adjust if using a different port).

## Testing Locally

1. **Run tests**:

    ```bash
    pytest test.py
    ```

2. **Check code style**:

    Ensure your code adheres to Python styling standards:

    ```bash
    pylint main
    ```

## Setting Up Kubernetes Locally

1. **Install Minikube**:

   Follow the official [Minikube installation guide](https://minikube.sigs.k8s.io/docs/start/).

2. **Start Minikube**:

    ```bash
    minikube start
    ```

3. **Configure Docker to use Minikube’s Docker daemon (optional)**:

   This setup allows direct image usage in Minikube:

    ```bash
    eval $(minikube docker-env)
    ```

## Deploying to Kubernetes

1. **Build Docker Image**:

   Ensure Docker is running, then build the image:

    ```bash
    docker build -t your-image-name .
    ```

2. **Create a namespace and deploy in Kubernetes cluster**:
   Create using `kubectl`:

    ```bash
    kubectl create ns web
    ```

   Deploy using `helm`:

    ```bash
    helm upgrade --install fastapi -n web -f values.yaml fastapi/
    ```

   Ensure the paths for `fastapi` helm chart is correct.

3. **Access your application**:

   Use `kubectl` to check the pod and service of the application:

    ```bash
    kubectl get po -n web
    kubectl get svc -n web
    ```

---

### Additional Notes

- **Customizing Deployments**: Use Helm charts or modify `values.yaml` for more complex configuration.
- **Troubleshooting**: View Kubernetes logs via `kubectl logs <pod-name>` if issues arise.
