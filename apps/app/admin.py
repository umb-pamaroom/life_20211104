from django.contrib import admin
from .models import Memo, RoutineModel, TimelineModel, Task
# 管理画面でデータをインポート・エクスポート
from import_export import resources
from import_export.admin import ImportExportMixin


class MemoResource(resources.ModelResource):
    class Meta:
        model = Memo

class MemoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MemoResource


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
admin.site.register(TimelineModel, TimelineModelAdmin)
admin.site.register(Task, TaskAdmin)
