from django.db import models

# Define possible states
STATE_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]

class Workflow(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='pending')

    def __str__(self):
        return self.name

class Task(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='pending')

    def __str__(self):
        return f"{self.name} - {self.state}"

class Link(models.Model):
    source = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="outgoing_links")
    target = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="incoming_links")

    def __str__(self):
        return f"{self.source.name} → {self.target.name}"
