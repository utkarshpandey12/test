from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from datetime import datetime

# Create your views here.


class Tasks(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serailzer = TaskSerializer(data=request.data)

        if serailzer.is_valid():
            if (
                datetime.strptime(
                    request.data["due_date"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ).timestamp()
                - datetime.now().timestamp()
            ) <= 0:
                return Response({"error": "due date has to be in future"}, status=400)
            serailzer.save()
            return Response(serailzer.data, status=200)

        return Response(serailzer.errors, status=400)


class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serailzer = UserSerializer(data=request.data)

        if serailzer.is_valid():
            serailzer.save()
            return Response(serailzer.data, status=200)

        return Response(serailzer.errors, status=400)
