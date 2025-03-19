# supplios_tech_task
 This is a CLI based hiring state machine , This machine have one workflow called Hiring , 
 and the tasks related to the hiring workflow are call, technical interview, assignment, offer.
 I will explain all the details below.

### How does my state machine works :

Workflow: Hiring
Tasks: [
   Call,
   Technical Interview,
   Assignment,
   Offer
]
States: [
   Pending,
   In Progress,
   Completed
]

flow:
   
   - When we start the 'Hiring' to 'in_progress' state , the first task auto trigger and moves to 'in_progress'.
   - But all other tasks like Technical Interview, Assignment,Offer are in 'pending' by default.
   - When the 'Call' changes its state from 'in_progres' to 'completed', it trigger the next task 'technical interview ' to 'in_progress'.
   - Likely , at the end when the last task  'offer' change its state from 'in_progess' to 'completed' , and workflow 'hiring'
     changes it state form 'in_progress' to 'complete'.

# features :

Create and manage workflow.
Add tasks aad manage its state.
Define link between each states , make it easy to transfer from one state to another.
Features build in REST Api.

# Technologies used:

Django
Django REST Framework
SQLite(database)
pytest(for test)

# **Installation:**

1. Clone the gitrepo
    `git clone git@github.com:binibenny95/supplios_tech_task.git
    cd supplios_tech_task`
2. Create a virtual environment(but it's optional)
   ` python3 -m venv venv
    source venv/bin/activate # on Linux`
3. Install all packages required for the project.
   `pip install -r requirements.txt`
4. Run Migrations
   ` python manage.py migrate`
5. Run the developement server
  ` python manage.py runserver `
  (since we dont have UI , i used terminal/postman to test)
6. create a superuser(optional)
   ` python manage.py createsuperuser`
   
 You  can Access the admin interface at http://127.0.0.1:8000/admin/ 
 to create workflows, tasks, and links.

# ****Test via Python shell****

(python manage.py runserver should be running)
1. `python manage.py shell`
2. inside the shell , import workflow, link,task models.

`   from workflow.models import Workflow, Task, Link
   from workflow.services import update_task_state, start_workflow, update_workflow_state `
3. Create a workflow with the default state (pending)
   
    `workflow = Workflow.objects.create(name="Hiring Workflow")
    print(workflow)  # Should print: Hiring Workflow`
4.  verify state 
     `print(workflow.state) ` # Expected output: 'pending'

5. create tasks under the workflow.

`task1 = Task.objects.create(workflow=workflow, name="Call", state="pending")
task2 = Task.objects.create(workflow=workflow, name="Technical Interview", state="pending")
task3 = Task.objects.create(workflow=workflow, name="Assignment", state="pending")
task4 = Task.objects.create(workflow=workflow, name="Offer", state="pending")`

6.` print(Task.objects.all()) ` # verify tasks.

7.  Define link between the tasks together.

  ` Link.objects.create(source=task1, target=task2)
Link.objects.create(source=task2, target=task3)
Link.objects.create(source=task3, target=task4)`

8.Start the workflow. sate of  task 'call' cahnges from 'pending'' to 'in_progress'.
  ` start_workflow(workflow)`
  ` workflow.refresh_from_db()
   print(workflow.state)`  # Expected output: in_progress

  ` task1.refresh_from_db()
   print(task1.state)`  # Expected output: in_progress

9. Complete task1 and verify if task2 moves to "in_progress" automatically.
   `update_task_state(task1, "completed")`
    
     `task1.refresh_from_db()
     task2.refresh_from_db()`

     `print(task1.state)`  # Expected output: 'completed'
     `print(task2.state)`  # Expected output: 'in_progress'
10. Repeat this for till task4 , once all tasks are completed workflow hiring state changes from 'in_progres' to 'completed'.
    
    `update_task_state(task2, "completed")
    update_task_state(task3, "completed")
    update_task_state(task4, "completed")`
  ` workflow.refresh_from_db()`
   `print(workflow.state) ` # Expected output: 'completed'


# **API Endpoints(Test with Postman):**

Workflows:
1.Create Workflow
   POST /api/workflows/
   request body:
   {"name": "Hiring"}
2. create Tasks
   POST /api/tasks/
   request body:
   {"workflow": 1, "name": "Call"}
 
   Repeat for Technical Interview, Assignment, and offer.
3. Create Links
   POST /api/links/
   {"source": 1, "target": 2}
   Repeat for the next tasks.

4. Start a workflow.
   POST /api/workflows/1/update_state/
   {"state": "in_progress"} 
   
Workflow moves to in_progress.First task call moves to in_progress.

5.POST /api/tasks/1/update_state/
  {"state": "completed"}
  Task Call moves to completed.
  Task Technical Interview moves to in_progress.

Continue updating each task's state, and
once Offer is completed, the workflow should be marked as completed.

### Improvements:

1. UI to handle create,update,delete task, workflows,links.
2. What will happens if there is two work flows , like once the hiring done it should auto trigger the next workflow onboarding .
3. A logging system like notifications/email to the admin whenever there is a change in task state and once the workflow completes.
4. Can on task have multiple subtasks and states ?
5. we can use django-fsm for state machine while creating models.






 
