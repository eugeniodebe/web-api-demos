# web-api-demos

This project contains a simple FastAPI backend packaged in Docker, intended for testing and deploying via **AWS App Runner** using a container from **Amazon ECR**.

## 🧪 Local Development

Create a conda environment (optional):

conda create -n fastapi-env python=3.12  
conda activate fastapi-env  
pip install fastapi uvicorn  
pip freeze > requirements.txt

Run the app locally:

uvicorn main:app --reload

Then open [http://localhost:8000](http://localhost:8000)

---

## 🐳 Build Docker Image Locally

docker build -t fastapi-app .

---

## ☁️ Deploy to AWS App Runner via Amazon ECR

### 1. Create ECR Repository

aws ecr create-repository --repository-name web-api-demos --region eu-west-2

### 2. Authenticate Docker to ECR

aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 975559947285.dkr.ecr.eu-west-2.amazonaws.com

### 3. Tag Docker Image

docker tag fastapi-app:latest 975559947285.dkr.ecr.eu-west-2.amazonaws.com/web-api-demos:latest

### 4. Push to ECR

docker push 975559947285.dkr.ecr.eu-west-2.amazonaws.com/web-api-demos:latest

---

### 5. Deploy in App Runner (via Console)

1. Go to https://console.aws.amazon.com/apprunner  
2. Choose "Container registry" as the source  
3. Select "Amazon ECR"  
4. Use image URI:  
   975559947285.dkr.ecr.eu-west-2.amazonaws.com/web-api-demos:latest  
5. Set port to 8000  
6. Click "Create & deploy"

---

## ✅ Result

App Runner will generate a public HTTPS endpoint like:

https://web-api-demos-xxxxxxxxx.eu-west-2.awsapprunner.com/

Your FastAPI app is now live on AWS 🚀
