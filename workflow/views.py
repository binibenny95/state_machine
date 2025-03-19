from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Workflow, Task, Link
from .serializers import WorkflowSerializer, TaskSerializer, LinkSerializer
from .services import update_task_state, start_workflow


class WorkflowViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows workflows to be viewed or edited.
    '''
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer

    @action(detail=True, methods=['post'])
    def update_state(self, request, pk=None):
        '''
         This method used for update the workflow based on user input.
        '''
        workflow = self.get_object()
        new_state = request.data.get("state")

        #state validation.
        if new_state not in ["pending", "in_progress", "completed", "rejected"]:
            return Response(
                {"error": "Invalid state. Choose pending, in_progress, completed, or rejected"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if new_state == "in_progress":
            if workflow.state == "rejected":
                return Response({"error": "Cannot start a rejected workflow"}, status=status.HTTP_400_BAD_REQUEST)
            if workflow.state == "pending":
                start_workflow(workflow)

        return Response(WorkflowSerializer(workflow).data)


class TaskViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows tasks to be viewed or edited.
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def update_state(self, request, pk=None):
        '''
        This method used for update the task based on user input.
        '''
        task = self.get_object()
        new_state = request.data.get("state")

       # state validation.
        if new_state not in ["pending", "in_progress", "completed", "rejected"]:
            return Response({"error": "Please enter a valid state like in_progress, completed, rejected"}, status=status.HTTP_400_BAD_REQUEST)

        if new_state == "rejected":
            # Prevent completing a rejected task
            if task.state == "completed":
                return Response(
                    {"error": "Cannot reject a completed task"}, status=status.HTTP_400_BAD_REQUEST
                )
        #update the state by the fun update_task_state in services.py
        update_task_state(task, new_state)
        return Response(TaskSerializer(task).data)


class LinkViewSet(viewsets.ModelViewSet):
    '''
      API endpoint that allows links between tasks to be managed.
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
