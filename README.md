
# 📝 Serverless To-Do List App on AWS

## 📌 Overview
This project is a **serverless CRUD API** for managing a to-do list using **AWS services**.  
It includes a static frontend hosted on Amazon S3 and a fully managed backend using Lambda, API Gateway, and DynamoDB.

> ✅ This project is based on the AWS Solutions Architect Associate.

---
## 🧱 Architecture

![Architecture](aws-serverless-todo-api/architecture-diagram.png.PNG)

---

### 🔄 Components
- **Frontend**:  
  Static HTML + JS website hosted on Amazon S3  ِِ
  (communicates with the backend using fetch + REST API)

- **API Gateway**:  
  Exposes 4 REST endpoints (POST, GET, PUT, DELETE)

- **AWS Lambda**:  
  Backend logic for each CRUD operation

- **Amazon DynamoDB**:  
  NoSQL table to store tasks using `taskId` as partition key

- **Amazon SNS**:  
  Sends notification when a new task is created

- **CloudWatch + X-Ray**:  
  Monitors and traces requests and logs

---

## 🚀 Features

- ✅ Create, Read, Update, Delete tasks
- ✅ Event-driven architecture with SNS
- ✅ Full-stack: frontend + backend
- ✅ Monitoring & observability using CloudWatch and X-Ray

---

## 🛠 Technologies Used

| Service        | Purpose                          |
|----------------|----------------------------------|
| S3             | Static website hosting           |
| API Gateway    | REST API exposure                |
| AWS Lambda     | Serverless backend (Python)      |
| DynamoDB       | NoSQL database                   |
| SNS            | Notifications (email)            |
| CloudWatch     | Logs + Metrics                   |
| X-Ray          | Request tracing                  |

---

## 📮 API Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | /tasks           | Create new task     |
| GET    | /tasks           | Get task            |
| PUT    | /tasks/{id}      | Update task by ID   |
| DELETE | /tasks/{id}      | Delete task by ID   |

---

## 🗂 Project Structure

```
aws-serverless-todo-api/
├── backend/
│   ├── create_task.py
│   ├── get_task.py
│   ├── update_task.py
│   ├── delete_task.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── main.js
│
├── architecture-diagram.png
├── README.md
```

---

## 🧪 How to Use (Quick Start)

1. Deploy the Lambda functions with correct IAM permissions
2. Create API Gateway routes and integrate with Lambda
3. Deploy static frontend to S3 bucket with public read
4. Test using browser or Postman
5. Check CloudWatch logs and SNS notifications

---

## 👤 Author

**Mohamed Alaa**  
📧 Email: [malaa20499@gmail.com]
🔗 LinkedIn: [https://www.linkedin.com/in/mohamed-alaa-37672a18b](#)

---

## 🏁 Final Notes

This project demonstrates:
- Real-world use of serverless patterns
- Scalable, event-driven APIs
- Full AWS lifecycle: compute, storage, monitoring, security
