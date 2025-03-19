# Employee Hiring - State Machine/Workflow Engine

## Overview
This is a CLI based State machine consisting of Workflows/Tasks in an Employee Hiring process.It has one workflow called **Hiring** and its associated Tasks.

- **Workflow** : Hiring
- **Tasks** :
  - Introduction Call
  - Technical Interview
  - Technical Assessment
  - Job Offer
- **States** :
  - pending
  - in_progress
  - completed

## Technology Stack

This State Engine is developed using **Python** as the Coding Language. Other technologies used along with Python are mentioned below:

1. Django
2. Django REST Framework
3. SQLite (Database)
4. Pytest (For code testing)
5. PyCharm (IDE)
6. Git/GitHub ( Version Control System)

## Code Features

- Create and manage workflow.
- Add Tasks and manage its States.
- Define link between each States , make it easy to transfer from one state to another.
- Features are built in REST API.

flow:
   
   - When we start the 'Hiring' to 'in_progress' state , the first task auto trigger and moves to 'in_progress'.
   - But all other tasks like Technical Interview, Assignment,Offer are in 'pending' by default.
   - When the 'Call' changes its state from 'in_progres' to 'completed', it trigger the next task 'technical interview ' to 'in_progress'.
   - Likely , at the end when the last task  'offer' change its state from 'in_progess' to 'completed' , and workflow 'hiring'
     changes it state form 'in_progress' to 'complete'.


## System Pre-requisites

- Python and PIP should be available.
- All other requirements will be installed using pip

## Steps to use the code

1. Make a local copy of the code by cloning it from the GitHub Repository.

    `git clone git@github.com:binibenny95/supplios_tech_task.git`
2. Change working directory to supplios_tech_task and create python virtual environment (recommended but optional)

    `cd supplios_tech_task`

   ` python3 -m venv venv`
3. Source virtual environment 

    `source venv/bin/activate`
4. Install all required packages for this project

   `pip install -r requirements.txt`
5. Run Migrations

    `python manage.py migrate`
6. Run the development server

    `python manage.py runserver`

   - (since we dont have UI , I have used terminal/postman to test)
7. Create a superuser(optional)

   `python manage.py createsuperuser`
   
 You  can Access the admin interface at http://127.0.0.1:8000/admin/ 
 to create workflows, tasks, and links.

## Code Testing

### Testing via Python Shell

(python manage.py runserver should be running)
1. Make sure that python manage.py runserver is running and start the Python shell
    `python manage.py shell`

2. Inside the shell, import workflow,links and task models.

         from workflow.models import Workflow, Task, Link
   
         from workflow.services import update_task_state, start_workflow, update_workflow_state
3. Create a workflow with the default state (pending)
   
         workflow = Workflow.objects.create(name="Hiring Workflow")

         print(workflow)  # Should print: Hiring Workflow
4.  Verify the State.

         print(workflow.state)

         #Expected output: 'pending'

5. Create tasks under the workflow.
                              
       task1 = Task.objects.create(workflow=workflow, name="Introduction Call", state="pending")
       
       task2 = Task.objects.create(workflow=workflow, name="Technical Interview", state="pending")
       
       task3 = Task.objects.create(workflow=workflow, name="Technical Assessment", state="pending")
       
       task4 = Task.objects.create(workflow=workflow, name="Job Offer", state="pending")

6. Verify the tasks.

       print(Task.objects.all())

7.  Define links between the tasks.

        Link.objects.create(source=task1, target=task2)
        Link.objects.create(source=task2, target=task3)
        Link.objects.create(source=task3, target=task4)

8. Start the workflow. State of the Task 'Introduction Call' changes from 'pending'' to 'in_progress'.

       start_workflow(workflow)
       workflow.refresh_from_db()
       print(workflow.state)# Expected output: in_progress

       task1.refresh_from_db()
       print(task1.state)`  # Expected output: in_progress

9. Complete Task1 and verify if Task2 moves to "in_progress" automatically.

       update_task_state(task1, "completed")
    
       task1.refresh_from_db()
       task2.refresh_from_db()`

       print(task1.state) # Expected output: 'completed'
       print(task2.state) # Expected output: 'in_progress'

10. Repeat above steps till task4 , once all tasks are completed, the state of workflow Hiring changes from 'in_progres' to 'completed'.
    
        update_task_state(task2, "completed")
        update_task_state(task3, "completed")
        update_task_state(task4, "completed")
        workflow.refresh_from_db()
        print(workflow.state) # Expected output: 'completed'


### API Endpoints(Testing with Postman)

1. Create Workflow
   - POST /api/workflows/
   - Request body: {"name": "Hiring"}
2. Create Tasks
   - POST /api/tasks/
   - Request body: {"workflow": 1, "name": "Call"}

3. Repeat for Technical Interview, Technical Assessment and Job Offer tasks.
4. Create Links
   - POST /api/links/
   - {"source": 1, "target": 2}
5. Repeat the same for the next tasks.
6. Start a workflow.
   - POST /api/workflows/1/update_state/
   - {"state": "in_progress"} 
   
7. Workflow moves to in_progress.First Task - Introduction Call moves to in_progress.

8. Update State of Task 1 as completed 
   - POST /api/tasks/1/update_state/
   - {"state": "completed"}
9. Task Call moves to completed and hence the task Technical Interview moves to in_progress.

10. Continue updating each task's state.Once the state of last task Job Offer is updated as completed, then the state of overall workflow should be automatically changed to completed.

# Potential Improvements:

1. UI to handle create,update,delete task, workflows,links.
2. What will happens if there is two work flows , like once the hiring done it should auto trigger the next workflow onboarding .
3. A logging system like notifications/email to the admin whenever there is a change in task state and once the workflow completes.
4. Can on task have multiple subtasks and states ?
5. we can use django-fsm for state machine while creating models.






 
