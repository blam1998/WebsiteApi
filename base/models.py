from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.TextField()
    desc = models.TextField(null = True, blank = True)
    def __list__(self):
        return [self.name, self.desc]
    


class User(models.Model):
    userId = models.TextField()
    tasks = models.ManyToManyField(Tasks, through = "UserTasksUnion")
    def __list__(self):
        return [self.userId, self.tasks]

class UserTasksUnion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userTasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
