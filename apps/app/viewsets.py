from rest_framework import viewsets, filters
from .models import *
from .serializers import TimelineSerializer
from django.db.models import Q

# 保存などの時や表示はここに書く
class TimelineViewSet(viewsets.ModelViewSet):
    queryset = TimelineModel.objects.all()
    serializer_class = TimelineSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title')

    # ログインユーザのタイムラインのみを表示　
    def get_queryset(self):
        return TimelineModel.objects.filter(Q(create_user=self.request.user) | Q(members__in=[self.request.user])).distinct().order_by('-updated_datetime', '-created_datetime')

    def perform_create(self, serializer):
        # The request user is set as author automatically.
        serializer.save(create_user=self.request.user)
