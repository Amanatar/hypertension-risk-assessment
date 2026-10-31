import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

def test_homepage_loads():
    app.config["TESTING"] = True
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
