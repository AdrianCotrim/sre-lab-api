# sre-lab-api

A simple item management API (basic CRUD) built to demonstrate a straightforward SRE/DevOps architecture, including containerization, Kubernetes, and CI/CD.

---

## 🧭 Project Overview

This project is not focused on application complexity, but rather on the infrastructure surrounding it.

Dev → GitHub → GitHub Actions → Docker → Registry → Kubernetes (Minikube)

---

## 🚀 Purpose

Simulate a real-world production environment with:

- Simple API (Flask)
- Automated testing (pytest)
- Containerization (Docker)
- Local orchestration (Minikube + Kubernetes)
- CI/CD pipeline (GitHub Actions)

---

## 🧠 Application

### Endpoints

Health Check:

GET /health

Response:

```json
{
  "status": "ok"
}
```

GET /items

```json
[
  { "name": "item1" },
  { "name": "item2" }
]
```

POST /items

Request Body:

```json
{
  "name": "item 1"
}
```

---

## ⚙️ Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🐳 Docker

```bash
docker build -t sre-lab-api .
docker run -p 5000:5000 sre-lab-api
```

With a volume:

```bash
docker run -p 5000:5000 -v $(pwd):/app sre-lab-api
```

---

## 🧩 Docker Compose

```bash
docker compose up
```

---

## ☸️ Kubernetes (Minikube)

```bash
minikube start
```

Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sre-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sre-api
  template:
    metadata:
      labels:
        app: sre-api
    spec:
      containers:
        - name: api
          image: sre-lab-api:latest
          ports:
            - containerPort: 5000
```

Service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sre-api-service
spec:
  selector:
    app: sre-api
  ports:
    - port: 80
      targetPort: 5000
  type: NodePort
```

ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  ENV: "production"
```

Horizontal Pod Autoscaler (HPA):

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: sre-lab-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: sre-api
  minReplicas: 2
  maxReplicas: 5
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
```

---

## 🔁 CI/CD (GitHub Actions)

Pipeline:

**Test → Build → Scan → Push → Deploy**

Steps:

- Checkout code: `actions/checkout@v4`
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `PYTHONPATH=. pytest`
- Start Minikube:
  ```bash
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  minikube start --driver=docker
  ```
- Deploy:
  ```bash
  kubectl apply -f deployment.yaml
  ```

---

## 🧠 Concepts Demonstrated

- Twelve-Factor App principles
- Immutable containers
- Infrastructure as Code (IaC)
- Basic GitOps
- Automated CI/CD
- Declarative Kubernetes
- Basic observability

---

## 🧑‍💻 Adrian Cotrim

A study project focused on modern SRE and DevOps practices.
