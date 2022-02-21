from rest_framework import serializers
from .models import *


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineModel
        # idは削除時に特定するために必ず必要
        fields = ['id','title', 'description','create_user','members']
