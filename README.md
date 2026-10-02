# Machine Learning Zoomcamp 2026

Este repositorio contiene mis notas de estudio, ejercicios prácticos, tareas (*homework*) y proyectos desarrollados durante el curso **[Machine Learning Zoomcamp 2026](https://github.com/DataTalksClub/machine-learning-zoomcamp)** impartido por **DataTalks.Club**.

---

## 📌 Estructura del Repositorio

- **`01-intro/`** — Introducción a Machine Learning y preparación del entorno.
- **`02-regression/`** — Modelos de regresión y predicción de precios.
- **`03-classification/`** — Modelos de clasificación y predicción de abandono (*churn*).
- **`04-evaluation/`** — Métricas de evaluación para modelos de clasificación.
- **`05-deployment/`** — Despliegue de modelos como servicios web (FastAPI, Docker).
- **`06-trees/`** — Árboles de decisión, Random Forest y Gradient Boosting.
- **`midterm-project/`** — Proyecto intermedio (*Midterm Project*).
- **`08-deep-learning/`** — Redes neuronales y Deep Learning para visión computacional.
- **`09-serverless/`** — Despliegue de modelos en entornos *Serverless* (AWS Lambda).
- **`10-kubernetes/`** — Despliegue y escalado con Kubernetes y TensorFlow Serving.
- **`capstone-project/`** — Proyecto final (*Capstone Project*).

---

## 🛠️ Tecnologías y Entorno

El proyecto está gestionado con **[uv](https://github.com/astral-sh/uv)** para la administración rápida y reproducible de dependencias y entornos virtuales de Python.

- **Python:** 3.11
- **Librerías principales:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `jupyterlab`, `ipykernel`.

---

## 🚀 Cómo reproducir este entorno

1. Clonar el repositorio.
2. Instalar las dependencias sincronizadas con `uv`:
   ```bash
   uv sync
   ```
3. Iniciar JupyterLab:
   ```bash
   uv run jupyter lab
   ```
