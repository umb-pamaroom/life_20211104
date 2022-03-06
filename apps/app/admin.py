from django.contrib import admin
from .models import *
# 管理画面でデータをインポート・エクスポート
from import_export import resources
from import_export.admin import ImportExportMixin


class MemoResource(resources.ModelResource):
    class Meta:
        model = Memo

class MemoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MemoResource


class TaskProjectModelResource(resources.ModelResource):
    class Meta:
        model = TaskProjectModel

class TaskProjectModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TaskProjectModelResource


class TaskSectionModelResource(resources.ModelResource):
    class Meta:
        model = TaskSectionModel


class TaskSectionModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TaskSectionModelResource



# 管理画面でインポート・エクスポート
class RoutineModelResource(resources.ModelResource):
    class Meta:
        model = RoutineModel

class RoutineModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RoutineModelResource



# 管理画面でインポート・エクスポート
class TimelineModelResource(resources.ModelResource):
    class Meta:
        model = TimelineModel

class TimelineModelAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TimelineModelResource



# 管理画面でインポート・エクスポート
class TaskResource(resources.ModelResource):
    class Meta:
        model = Task

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TaskResource


    
admin.site.register(Memo, MemoAdmin)
admin.site.register(RoutineModel, RoutineModelAdmin)
admin.site.register(TaskSectionModel, TaskSectionModelAdmin)
admin.site.register(TaskProjectModel, TaskProjectModelAdmin)
admin.site.register(TimelineModel, TimelineModelAdmin)
admin.site.register(Task, TaskAdmin)