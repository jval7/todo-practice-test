from fastapi.testclient import TestClient
from app import main
from app.api import routers


def test_should_generate_save_document_when_calling_save_document_ep():
    # configurations
    client = TestClient(main.app)
    document = routers.DocumentInput(content="hello world")
    # action
    response = client.post(url="/save-document/", json=document.model_dump())
    # assert
    assert response.status_code == 201
    assert response.json() == {"status": "Document saved successfully"}
