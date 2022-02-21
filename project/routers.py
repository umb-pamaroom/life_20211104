from rest_framework import routers
from apps.calendar.viewsets import TaskViewSet
from apps.app.viewsets import *

router = routers.DefaultRouter()

router.register('month_with_forms', TaskViewSet)
router.register('timeline', TimelineViewSet)
