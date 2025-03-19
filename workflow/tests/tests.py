# workflow_engine/tests/test_views.py

import pytest
from rest_framework.test import APIClient
from workflow.models import Workflow, Task, Link


@pytest.mark.django_db
def test_create_workflow():
    client = APIClient()
    response = client.post("/api/workflows/", {"name": "Hiring"}, format="json")
    assert response.status_code == 201
    assert response.data['name'] == "Hiring"


@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    workflow = Workflow.objects.create(name="Hiring")
    response = client.post("/api/tasks/", {"name": "Call", "workflow": workflow.id}, format="json")
    assert response.status_code == 201
    assert response.data['name'] == "Call"
    assert response.data['workflow'] == workflow.id


@pytest.mark.django_db
def test_create_link():
    client = APIClient()
    workflow = Workflow.objects.create(name="Hiring")
    task1 = Task.objects.create(name="Call", workflow=workflow)
    task2 = Task.objects.create(name="Technical Interview", workflow=workflow)

    response = client.post("/api/links/", {"source": task1.id, "target": task2.id}, format="json")
    assert response.status_code == 201
    assert response.data['source'] == task1.id
    assert response.data['target'] == task2.id


@pytest.mark.django_db
def test_workflow_start():
    client = APIClient()
    workflow = Workflow.objects.create(name="Hiring")
    response = client.post(f"/api/workflows/{workflow.id}/update_state/", {"state": "in_progress"}, format="json")
    assert response.status_code == 200
    assert response.data['state'] == "in_progress"
