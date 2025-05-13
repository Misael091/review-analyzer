# 📝 Review Analyzer

A sentiment analysis API for processing user reviews using FastAPI. This microservice supports token-based authentication and is designed to be containerized with Docker.

---

## 🚀 Features

- JWT-based authentication system
- Analyze sentiment from user-submitted reviews
- Containerized with Docker and `docker-compose`
- Pytest-based unit and API tests

---

## 📁 Project Structure

```
review-analyzer/
├── app/
│   ├── main.py              # Entry point for FastAPI
│   ├── routers/
│   │   ├── auth.py          # Auth endpoints
│   │   └── review.py        # Review analysis endpoints
│   └── tests/               # Test suite
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build file
├── docker-compose.yml       # Docker orchestration
├── README.md
└── pytest.ini
```

---

## ⚙️ Installation

### 🔧 Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/review-analyzer.git
   cd review-analyzer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   uvicorn app.main:app --reload
   ```

   Access the docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🐳 Docker Setup

To build and run using Docker:

```bash
docker-compose up --build
```

---

## 🔐 Authentication

Before using the `/review` endpoint, authenticate with:

```
POST /auth/token
```

**Payload**:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

You’ll receive a JWT token, which must be included as a Bearer token in subsequent requests.

---

## 💬 API Endpoints

### `POST /auth/token`
Authenticate user and return a JWT.

### `POST /review`
Submit a review for sentiment analysis.

**Headers**:
```
Authorization: Bearer <token>
```

**Body**:
```json
{
  "review": "I love this product!"
}
```

**Response**:
```json
{
  "sentiment": "positive"
}
```

---

## 🧪 Running Tests

```bash
pytest app/tests
```

---