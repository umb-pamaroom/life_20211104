from rest_framework import viewsets, filters
from apps.app.models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title')

    
