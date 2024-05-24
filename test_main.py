import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_invoice():
    invoice_data = {
        "id": 1,
        "number": "INV-001",
        "amount": 100.0,
        "instatus": "Paid",
        "date": "2023-06-10T15:40:00"
    }
    response = client.post("/addinvoice", json=invoice_data)
    assert response.status_code == 201
    assert response.json() == invoice_data

def test_get_single_invoice():
    response = client.get("/getbyid/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_invoice():
    updated_invoice_data = {
        "id": 1,
        "number": "INV-001",
        "amount": 150.0,
        "instatus": "Pending",
        "date": "2023-06-15T09:00:00"
    }
    response = client.put("/update_invoice/1", json=updated_invoice_data)
    assert response.status_code == 202
    assert response.json()["amount"] == 150.0

def test_delete_invoice():
    response = client.delete("/delete_invoice/1")
    assert response.status_code == 200

def test_get_nonexistent_invoice():
    response = client.get("/getbyid/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Invoice not found"

def test_update_nonexistent_invoice():
    non_existent_invoice_data = {
        "id": 10,
        "number": "INV-010",
        "amount": 200.0,
        "instatus": "Unpaid",
        "date": "2023-07-01T11:00:00"
    }
    response = client.put("/update_invoice/10", json=non_existent_invoice_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Invoice with this id not found"

def test_delete_nonexistent_invoice():
    response = client.delete("/delete_invoice/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Invoice with this id is either deleted or not found"
