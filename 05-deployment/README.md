# Module 5: Deploying Machine Learning Models

This directory contains the frozen lead-scoring deployment service and container configuration for Homework 5.

---

## 🚀 How to Run

### 1. Local Run with `uv`

```bash
uv sync --locked
uv run python smoke_test.py
uv run python solution_q3.py
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

In another terminal, test the prediction endpoint:

```bash
python q6_test.py
```

### 2. Container Run with Docker

```bash
docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
```

Health check and prediction test:

```bash
curl http://localhost:9696/health
python q6_test.py
```

---

## 📝 Homework 5 Answers

- **Q1 (Environment check):** `uv --version` -> `uv 0.12.10`
- **Q2 (Scikit-Learn locked version):** `1.7.2`
- **Q3 (Model prediction):** `0.533` (0.532994)
- **Q4 (API prediction):** `0.770` (0.769799)
- **Q5 (Dockerfile base image):** `python:3.11.15-slim-bookworm`
- **Q6 (Container prediction & health):** `0.770` (0.769799), `/health` returns `status: ok` and verified model checksum
