from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Tasks, User, UserTasksUnion
from .serializers import TasksSerializer, UserSerializer, UserTasksUnionSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404



@api_view(["POST"])
def addUser(request):
    reqId = request.data.get('id')
    user1 = User.objects.create(userId = reqId)
    serializer = UserSerializer(user1, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def getData(request):
    reqId = request.GET.get('id')
    confirm = get_object_or_404(User, userId = reqId)
    serializer = UserSerializer(confirm, many=False)
    return Response(serializer.data)


"""
@api_view(["PUT"])
def putTask(request):
    reqId = request.data.get('id')
    confirmId = get_object_or_404(User, userId = reqId)
    userSerializer = UserSerializer(confirmId, data = request.data)
    print(request.data)
    if userSerializer.is_valid():
        userSerializer.save()
        return Response(userSerializer.data)

    return Response(userSerializer.errors)
"""

@api_view(["PUT"])
def putTask(request):
    reqId = request.data.get('id')
    reqMethod = request.data.get("method")
    confirmId = get_object_or_404(User, userId = reqId)
    userSerializer = UserSerializer(confirmId, data = request.data)

    if userSerializer.is_valid() and reqMethod:
        userSerializer.update(confirmId, request.data.get("tasks"), reqMethod)
        return Response(userSerializer.data)

    return Response(userSerializer.errors)

"""
@api_view(["PUT"])
def addUser(request):
"""
