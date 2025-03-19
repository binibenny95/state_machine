from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet, TaskViewSet, LinkViewSet

router = DefaultRouter()
router.register(r'workflows', WorkflowViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'links', LinkViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
