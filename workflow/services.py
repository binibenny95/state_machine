def update_workflow_state(workflow):
    """ Update the workflow state based on its tasks states"""
    all_tasks = workflow.tasks.all()

    if any(task.state == "rejected" for task in all_tasks):
        workflow.state = "rejected"
    elif all(task.state == "completed" for task in all_tasks):
        workflow.state = "completed"
    elif any(task.state == "in_progress" for task in all_tasks):
        workflow.state = "in_progress"
    else:
        workflow.state = "pending"

    workflow.save()


def update_task_state(task, new_state):
    """ Update the task state and trigger next task based on links and user input """
    task.state = new_state
    task.save()

    if new_state == "rejected":
        # If a task is rejected, prevent next tasks from starting
        update_workflow_state(task.workflow)
        return

    # If a task moves to "completed", trigger the next task
    if new_state == "completed":
        next_tasks = task.outgoing_links.all()
        for link in next_tasks:
            if link.target.state == "pending":
                update_task_state(link.target, "in_progress")

    # Update workflow state based on task progress
    update_workflow_state(task.workflow)


def start_workflow(workflow):
    """ Start workflow and trigger the first task """
    workflow.state = "in_progress"
    workflow.save()

    # Find the first task and set it to in_progress
    first_task = workflow.tasks.order_by("id").first()
    if first_task and first_task.state == "pending":
        update_task_state(first_task, "in_progress")
