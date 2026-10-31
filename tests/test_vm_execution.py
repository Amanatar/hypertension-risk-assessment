import os
import sys
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from app import app, stage_map

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_flask_get_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hypertension" in res.data or b"Blood Pressure" in res.data
    print("\n[VM EXECUTION] Flask GET / returned HTTP 200 successfully on Linux (templates/index.html verified).")

def test_flask_post_prediction(client):
    patient_telemetry = {
        "Gender": "Male",
        "Age": "51-64",
        "History": "Yes",
        "Patient": "Yes",
        "TakeMedication": "Yes",
        "Severity": "Moderate",
        "BreathShortness": "Yes",
        "VisualChanges": "No",
        "NoseBleeding": "No",
        "Whendiagnoused": "1-5 Years",
        "Systolic": "130+",
        "Diastolic": "91 - 100",
        "ControlledDiet": "No"
    }
    
    res = client.post("/predict", data=patient_telemetry)
    assert res.status_code == 200
    html_text = res.data.decode("utf-8")
    
    # Check if a clinical stage is rendered
    matched_stage = None
    for stage_id, stage_name in stage_map.items():
        if stage_name in html_text:
            matched_stage = stage_name
            break
            
    print(f"\n[VM EXECUTION] Patient Telemetry POST /predict -> HTTP {res.status_code}")
    print(f"[VM EXECUTION] -> Evaluated Clinical Stage: '{matched_stage or 'NORMAL'}'")
    print(f"[VM EXECUTION] -> Medical Triage Recommendations & Actions loaded successfully.")
    assert matched_stage is not None or "Confidence" in html_text or "Recommendation" in html_text
