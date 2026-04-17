# sre-lab-api

Uma API simples de gerenciamento de itens (CRUD básico) construída como base para demonstrar uma arquitetura completa de SRE/DevOps, incluindo containerização, Kubernetes e CI/CD com segurança.

---

## 🧭 Visão do Projeto

Este projeto não foca na complexidade da aplicação, mas sim na infraestrutura ao redor dela.

Dev → GitHub → GitHub Actions → Docker → Registry → Kubernetes (Minikube)
                        ↓
                    Trivy Scan

---

## 🚀 Objetivo

Simular um ambiente real de produção com:

- API simples (Flask)
- Testes automatizados (pytest)
- Containerização (Docker)
- Orquestração local (Minikube + Kubernetes)
- Pipeline CI/CD (GitHub Actions)
- Segurança com scan de imagem (Trivy)

---

## 📦 Estrutura do Projeto

sre-lab-api/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── hpa.yaml
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci-cd.yml

---

## 🧠 Aplicação

### Endpoints

Health Check:
GET /health

Resposta:
{
  "status": "ok"
}

GET /items

POST /items
Body:
{
  "name": "item 1"
}

---

## ⚙️ Rodando Localmente

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

---

## 🧪 Testes

pytest

---

## 🐳 Docker

docker build -t sre-lab-api .
docker run -p 5000:5000 sre-lab-api

Com volume:
docker run -p 5000:5000 -v $(pwd):/app sre-lab-api

---

## 🧩 Docker Compose

docker compose up

---

## ☸️ Kubernetes (Minikube)

minikube start

Deployment:
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

Service:
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

ConfigMap:
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  ENV: "production"

HPA:
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler

---

## 🔁 CI/CD (GitHub Actions)

Pipeline:

Test → Build → Scan → Push → Deploy

Etapas:

- Run tests: pytest
- Build image: docker build -t ghcr.io/user/sre-api:${{ github.sha }}
- Security scan: trivy image sre-api
- Push image: docker push ghcr.io/user/sre-api:${{ github.sha }}
- Deploy: kubectl apply -f k8s/

---

## 🔐 Segurança

- Secrets no GitHub
- Nenhuma credencial no código
- Scan de vulnerabilidades com Trivy antes do deploy
- Imagem versionada por commit SHA

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

## 📈 Próximos Passos

- Ingress Controller + HTTPS (TLS)
- Prometheus + Grafana
- Logs centralizados (Loki / ELK)
- Helm Charts
- Blue/Green Deployment
- Canary Releases
- Terraform (infra cloud real)

---

## 🧑‍💻 Autor

Projeto de estudo focado em práticas modernas de SRE e DevOps.
