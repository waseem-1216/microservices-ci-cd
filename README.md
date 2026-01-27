🚀 End-to-End CI/CD for Cloud-Deployed Microservices
📌 Project Overview

This project demonstrates a real-world DevOps implementation of an end-to-end CI/CD pipeline for Dockerized Python microservices, deployed on the cloud using Render.

The primary goal of this project is to showcase DevOps practices such as automation, containerization, CI/CD pipelines, cloud deployment, and production debugging — rather than frontend complexity.

🧱 Architecture Overview
Developer Push (Git)
        ↓
GitHub Actions (CI/CD)
        ↓
Docker Build
        ↓
Docker Hub (Container Registry)
        ↓
Render Cloud Platform
        ↓
Live Microservices (Public URLs)


Each microservice is built, tested, containerized, and deployed independently, following a microservices-based architecture.

🛠️ Tech Stack

Language: Python

Framework: Flask

Containerization: Docker

CI/CD: GitHub Actions

Container Registry: Docker Hub

Cloud Platform: Render

Version Control: Git & GitHub

📦 Microservices
🔹 User Service

Handles user-related functionality.

Live URL

https://user-service-latest-wnbx.onrender.com/


Endpoints

/ – Service status

/health – Health check endpoint

/users – Returns list of users

🔹 Task Service

Handles task-related functionality.

Live URL

https://task-service-9jdf.onrender.com/


Endpoints

/ – Service status

/health – Health check endpoint

/tasks – Returns list of tasks

🔁 CI/CD Pipeline
Continuous Integration (CI)

Triggered automatically on every push to the main branch

Builds Docker images for each microservice

Validates Dockerfiles to catch build errors early

Continuous Deployment (CD)

Pushes Docker images to Docker Hub

Uses GitHub Secrets for secure authentication

Deployed on Render using Docker images

Supports zero-downtime redeploys

☁️ Cloud Deployment (Render)

Each microservice is deployed as a separate Render Web Service, enabling independent scaling and updates.

Key Production Considerations

Dynamic port binding using the $PORT environment variable

Health check endpoints for service monitoring

Manual redeploy handling when using mutable Docker tags (latest)

🧠 Key DevOps Learnings

Implemented multi-service CI/CD pipelines

Dockerized independent microservices

Managed secrets securely using GitHub Actions

Resolved Git conflicts using git pull --rebase

Debugged real-world cloud deployment issues

Understood cloud platform port and health-check requirements

Learned how CI/CD integrates with container registries and cloud platforms

🏆 Why This Project Matters

This project mirrors real DevOps workflows seen in production environments:

Infrastructure as Code mindset

Automation-first deployment strategy

Cloud-native application design

Hands-on debugging of production issues

It goes beyond tutorials and demonstrates job-ready DevOps skills.

🔗 Live Services

User Service:
https://user-service-latest-wnbx.onrender.com/

Task Service:
https://task-service-9jdf.onrender.com/

📌 Future Enhancements

Versioned Docker image tags (v1.0.0, v1.0.1)

Automated redeploy hooks

API Gateway using Nginx

Centralized logging and monitoring

Kubernetes deployment

👤 Author

Waseem Ali
Aspiring DevOps Engineer

GitHub: https://github.com/waseem-1216/

LinkedIn: https://www.linkedin.com/in/waseem-ali-a61088228/

⭐ If You Find This Useful

Feel free to ⭐ star the repository or connect with me on LinkedIn.
