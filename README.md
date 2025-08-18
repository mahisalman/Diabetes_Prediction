# 🩺 Diabetes Prediction API
## 🚀 Live Demo: [Diabetes Prediction API](https://diabetes-prediction-6z0g.onrender.com/)
## 📖 Interactive Docs: [Swagger UI](https://diabetes-prediction-6z0g.onrender.com/docs)

A production-ready FastAPI-based web application for predicting diabetes risk using patient health data. This project demonstrates machine learning deployment, API design, and modern UI integration to make healthcare predictions accessible via a simple dashboard and REST API.
A machine learning-powered FastAPI web application that predicts diabetes risk from patient health data.

## The project includes:

A trained ML model (PIMA Diabetes dataset)

REST API endpoints for predictions, health checks & metrics

A dashboard-like frontend built with HTML/CSS/JS

Docker support for easy deployment

Hosted API ready for real-world use

## 🧪 Tech Stack

Backend: FastAPI

Model: Scikit-learn (Logistic Regression / Random Forest)

Frontend: HTML5, CSS3, Vanilla JS (custom-styled dashboard)

Deployment: Docker + Render

Monitoring: /metrics endpoint (JSON format)

## ✨ Features

✅ Machine Learning Model – Trained on the PIMA Diabetes Dataset

✅ REST API Endpoints with FastAPI

✅ Swagger UI & ReDoc for interactive documentation

✅ Beautiful Web UI with dashboard-like design (HTML, CSS, JS)

✅ /metrics endpoint for monitoring & health checks

✅ Dockerized for easy deployment

✅ Hosted on Render with CI/CD
![Screenshot](https://github.com/mahisalman/Diabetes_Prediction/blob/main/Untitled.png)
## 📂 Project Structure
```diabetes-prediction-api/
│── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI application
│   ├── schemas.py            # Pydantic models for input validation
│   ├── diabetes_model.pkl    # Trained ML model
│   ├── metrics.json          # API metrics
│   ├── requirements.txt      # Dependencies
│   ├── static/               # Frontend files
│   │   ├── index.html        # Web UI
│   │   ├── script.js         # UI logic
│   │   └── style.css         # Dashboard styling
│── data/
│   └── diabetes.csv          # Dataset for training
│── model/
│   ├── train_model.py        # ML training script
│── Dockerfile                # Docker build file
│── docker-compose.yml        # Docker Compose setup
│── requirements.txt          # Root dependencies
│── metrics.json              # Monitoring metrics
│── README.md                 # Project documentation
```

## 🛠️ Local Development

Clone the repo and install dependencies:
```git clone https://github.com/yourusername/diabetes-prediction-api.git
cd diabetes-prediction-api
pip install -r requirements.txt
```

## 🐳 Run with Docker

Build and run with Docker:
```docker build -t diabetes-api .
docker run -p 8000:8000 diabetes-api
```