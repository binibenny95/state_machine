# workflow_engine/tests/test_services.py

import pytest
from workflow.models import Workflow, Task
from workflow.services import update_task_state, update_workflow_state

@pytest.mark.django_db
def test_update_task_state_triggers_next_task():
    workflow = Workflow.objects.create(name="Hiring")
    task1 = Task.objects.create(workflow=workflow, name="Call")
    task2 = Task.objects.create(workflow=workflow, name="Technical Interview")

    update_task_state(task1, "completed")

    task1.refresh_from_db()
    task2.refresh_from_db()

    assert task1.state == "completed"
    assert task2.state == "in_progress"

@pytest.mark.django_db
def test_update_workflow_state_completes_workflow():
    workflow = Workflow.objects.create(name="Hiring")
    task1 = Task.objects.create(workflow=workflow, name="Call")
    task2 = Task.objects.create(workflow=workflow, name="Technical Interview")
    task3 = Task.objects.create(workflow=workflow, name="Assignment")
    task4 = Task.objects.create(workflow=workflow, name="Offer")

    update_workflow_state(workflow)

    workflow.refresh_from_db()

    assert workflow.state == "in_progress"
