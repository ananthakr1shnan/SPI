# 🧠 Student Performance Indicator (SPI)

An **end-to-end Machine Learning project** showcasing a complete ML pipeline from data preprocessing to deployment using **Docker** and **Microsoft Azure**.

## 🌐 Live Demo

[Click here to open the deployed app](https://studentperfindicator.azurewebsites.net)

---

## 📌 Overview

This project predicts student performance based on academic and demographic features. It's built to demonstrate:

- Clean machine learning pipeline with modular design
- Deployment-ready Flask API
- Docker containerization
- CI/CD using GitHub Actions
- Live deployment on Azure Web App via Azure Container Registry (ACR)

---

## 🧰 Tech Stack Used

Python, Flask, scikit-learn, XGBoost, CatBoost, Docker, GitHub Actions, Microsoft Azure

---

## ⚙️ How It Works

1. **Preprocessing**: Clean and encode raw data using pandas, scikit-learn
2. **Model Training**: Train using ML algorithms like CatBoost & XGBoost
3. **API Development**: Serve model predictions through a Flask API
4. **Dockerization**: Containerized using a Dockerfile for easy deployment
5. **CI/CD**: GitHub Actions automates Docker builds and Azure deployment
6. **Deployment**: Hosted on Azure Web App (F1 Free Tier)

---

## 💻 Running Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/SPI.git
cd SPI

# Build Docker image
docker build -t spi:latest .

# Run the container
docker run -p 5000:5000 spi:latest
```

Now visit: [http://localhost:5000](http://localhost:5000)

---

