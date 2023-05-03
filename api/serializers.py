from rest_framework import serializers
from base.models import Tasks, User, UserTasksUnion

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'tasks']
    
    def update(self, instance, validated_data, method):
        if not method:
            return instance
        
        match method:
            case "Add":
                instance = self.addTask(instance, validated_data)
            case "Delete":
                instance = self.deleteTask(instance, validated_data)
            case "Update":
                instance = self.updateTask(instance, validated_data)

        instance.save()
        return instance
        

    
    def addTask(self, instance, validated_data):
        name1 = validated_data[0].get("name")
        desc1 = validated_data[0].get("desc")


        if name1:
            newTask = Tasks.objects.create(name = name1, desc = desc1)
            instance.tasks.add(newTask)
            instance.save()
        return instance
    
    def deleteTask(self, instance, validated_data):
        name1 = validated_data[0].get("name")
        desc1 = validated_data[0].get("desc")
        taskId = validated_data[0].get("id")

        taskObj = 0

        if name1 and desc1:
            taskObj = Tasks.objects.get(id = taskId, name = name1, desc = desc1)
        elif name1:
            taskObj = Tasks.objects.get(id = taskId, name = name1)
        
        instance.tasks.remove(taskObj)
        instance.save()

        return instance
    
    def updateTask(self, instance, validated_data):
        name1 = validated_data[0].get("name")
        desc1 = validated_data[0].get("desc")
        taskId = validated_data[0].get("id")

        taskObj = Tasks.objects.get(id = taskId)
        taskObj.name = name1
        taskObj.desc = desc1
        taskObj.save()

        instance.save()
        return instance





class UserTasksUnionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    userTasks = TasksSerializer(many=True)

    class Meta:
        model = UserTasksUnion
        fields = '__all__'

