# Clinical Hypertension Risk Assessment

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
