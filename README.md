# supplios_tech_task
 This is a CLI based hiring state machine , This machine have one workflow called Hiring , 
 and the tasks related to the hiring workflow are call, technical interview, assignment, offer.
 I will explain all the details below.

How does my state machine works :

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
features :
Create and manage workflow.
Add tasks nad manage its state.
Define link between each states , make it easy to transfer from one state to another.
Features build in REST Api.

Technologies used:
Django
Django REST Framework
SQLite(database)
pytest(for test)

Installation:

1. Clone the gitrepo
    git clone git@github.com:binibenny95/supplios_tech_task.git
    cd supplios_tech_task
2. Create a virtual environment(but it's optional)
    python3 -m venv venv
    source venv/bin/activate # on Linux
3. Install all packages required for the project.
   pip install -r requirements.txt
4. Run Migrations
    python manage.py migrate
5. Run the developement server
   python manage.py runserver 
  (since we dont have UI , i used postman to test)
6. create a superuser(optional)
    python manage.py createsuperuser
   
 You  can Access the admin interface at http://127.0.0.1:8000/admin/ 
 to create workflows, tasks, and links.

API Endpoints(Test with Postman):

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

Improvements:

1. UI to handle create,update,delete task, workflows,links.
2. What will happens if there is two work flows , like once the hiring done it should auto trigger the next workflow onboarding .
3. A logging system like notifications/email to the admin whenever there is a change in task state and once the workflow completes.
4. Can on task have multiple subtasks and states ?






 
