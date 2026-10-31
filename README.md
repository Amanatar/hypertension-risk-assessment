# Clinical Hypertension Risk Assessment

<div align="center">

[![CI Verified](https://github.com/Amanatar/hypertension-risk-assessment/actions/workflows/ci-verify.yml/badge.svg)](https://github.com/Amanatar/hypertension-risk-assessment/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

Production-oriented clinical risk stratification interface mapping multi-factor cardiovascular telemetry into four clinical stages: Normal, Stage-1 Hypertension, Stage-2 Hypertension, and Hypertensive Crisis.

## Architecture

- **Predictive Core:** Multiclass Logistic Regression classifier (`logreg_model.pkl`) trained on standard cardiovascular telemetry features (age, sex, BMI, BP history, lifestyle factors).
- **Inference Pipeline:** Robust input scaling and categorical encoding with boundary validation.
- **Web Interface:** Lightweight Flask app with interactive patient telemetry forms, immediate risk triaging, and clinical action guidelines.

## Project Structure

```
hypertension-risk-assessment/
├── app.py                # Flask server and inference routing
├── train_model.py        # Model training and calibration pipeline
├── logreg_model.pkl      # Serialized scikit-learn multiclass estimator
├── scaler.pkl            # Feature scaling transformer
├── templates/
│   └── index.html        # Responsive clinical telemetry UI
├── tests/
│   └── test_app_smoke.py # Flask client smoke tests
└── requirements.txt      # Python dependencies
```

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Or on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Run tests:
```bash
pytest tests/
```
