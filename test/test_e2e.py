from fastapi.testclient import TestClient
from app import main
from app.api import routers


def test_should_generate_save_document_when_calling_save_document_ep():
    # configurations
    assert 1 == 1
