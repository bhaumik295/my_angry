from django.test import TestCase
from .models import Task
from django.utils import timezone

class TaskModelTest(TestCase):
    
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now(),
            is_completed=False
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Task")
