from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Workflow, Task, Link
from .serializers import WorkflowSerializer, TaskSerializer, LinkSerializer
from .services import update_task_state, start_workflow


class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer

    @action(detail=True, methods=['post'])
    def update_state(self, request, pk=None):
        workflow = self.get_object()
        new_state = request.data.get("state")

        if new_state == "in_progress" and workflow.state == "pending":
            start_workflow(workflow)

        return Response(WorkflowSerializer(workflow).data)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def update_state(self, request, pk=None):
        task = self.get_object()
        new_state = request.data.get("state")

        if new_state not in ["pending", "in_progress", "completed"]:
            return Response({"error": "Invalid state"}, status=status.HTTP_400_BAD_REQUEST)

        update_task_state(task, new_state)
        return Response(TaskSerializer(task).data)


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
