# sre-lab-api

Uma API simples de gerenciamento de itens (CRUD básico) construída como para demonstrar uma arquitetura simples de SRE/DevOps, incluindo containerização, Kubernetes e CI/CD. 

---

## 🧭 Visão do Projeto

Este projeto não foca na complexidade da aplicação, mas sim na infraestrutura ao redor dela.

Dev → GitHub → GitHub Actions → Docker → Registry → Kubernetes (Minikube)

---

## 🚀 Objetivo

Simular um ambiente real de produção com:

- API simples (Flask)
- Testes automatizados (pytest)
- Containerização (Docker)
- Orquestração local (Minikube + Kubernetes)
- Pipeline CI/CD (GitHub Actions)

---

## 🧠 Aplicação

### Endpoints

Health Check:
GET /health

Resposta:

`{
  "status": "ok"
}`

GET /items

`{
  ["name": "item1"],
  ["name": "item2"]
}`

POST /items

Body:

`{
  "name": "item 1"
}`

---

## ⚙️ Rodando Localmente

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

## 🧪 Testes

`pytest`

---

## 🐳 Docker

```
docker build -t sre-lab-api .
docker run -p 5000:5000 sre-lab-api
```

Com volume:
`docker run -p 5000:5000 -v $(pwd):/app sre-lab-api`

---

## 🧩 Docker Compose

`docker compose up`

---

## ☸️ Kubernetes (Minikube)

`minikube start`

Deployment:
```
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
```
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
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  ENV: "production"
```

HPA:
```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: sre-lab-hpa
spec:
  scaleTargetRef:
    apiVersion: app/v1
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

Test → Build → Scan → Push → Deploy

Etapas:

- Checkout code: actions/checkout@v4
- Install dependencies: pip install -r requirements.txt
- Run tests: PYTHONPATH=. pytest
- Start Minikube: curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64  \
                  sudo install minikube-linux-amd64 /usr/local/bin/minikube  \
                  minikube start --driver=docker
- Deploy: kubectl apply -f deployment.yaml

---

## 🧠 Conceitos Demonstrados

- 12-factor app
- Containers imutáveis
- Infraestrutura como código (IaC)
- GitOps básico
- CI/CD automatizado
- Kubernetes declarativo
- Observabilidade base

---

## 🧑‍💻 Adrian Cotrim

Projeto de estudo focado em práticas modernas de SRE e DevOps.
