from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey('self', on_delete=models.PROTECT, related_name='sub_tasks', null=True)
