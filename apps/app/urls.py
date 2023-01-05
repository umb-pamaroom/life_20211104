from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('diary/', views.index, name='index'),

    # 自分の日記一覧
    path('mydiary/', views.mydiary, name='mydiary'),
    # path('mydiary/', views.MydiaryListView.as_view(), name='mydiary'),
    path('diary/<int:memo_id>', views.detail, name='detail'),
    # path('diary/date/<int:dateData>', views.detail, name='date'),
    path('diary/new_memo', views.new_memo, name='new_memo'),

    # 食事一覧
    path('diary/meal_list', views.meal_list, name='meal_list'),
    path('diary/breakfast_list', views.breakfast_list, name='breakfast_list'),
    path('diary/lunch_list', views.lunch_list, name='lunch_list'),
    path('diary/dinner_list', views.dinner_list, name='dinner_list'),
    
    path('diary/delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo'),
    path('diary/edit_memo/<int:memo_id>', views.edit_memo, name='edit_memo'),

    # ルーティーン
    path('routine/create/', views.RoutineCreateView.as_view(), name='RoutineCreate'),
    path('routine/detail/<int:pk>', views.RoutineDetailView.as_view(), name='RoutineDetail'),
    path('routine/delete/<int:pk>', views.RoutineDeleteView.as_view(), name='RoutineDelete'),
    path('routine/update/<int:pk>', views.RoutineUpdateView.as_view(), name='RoutineUpdate'),
    path('routine/list/', views.RoutineListView.as_view(), name='RoutineList'),

    # タイムライン
    path('timeline/create/', views.TimelineCreateView.as_view(), name='TimelineCreate'),
    path('timeline/detail/<int:pk>', views.TimelineDetailView.as_view(), name='TimelineDetail'),
    path('timeline/<int:pk>', views.TimelineItemsView.as_view(), name='TimelineItems'),
    path('timeline/delete/<int:pk>', views.TimelineDeleteView.as_view(), name='TimelineDelete'),
    path('timeline/update/<int:pk>', views.TimelineUpdateView.as_view(), name='TimelineUpdate'),
    path('timeline/share/<int:pk>', views.TimelineShareView.as_view(), name='TimelineShare'),
    path('timeline/', views.TimelineListView.as_view(), name='TimelineList'),
    path('uncheck_task', views.uncheck_task, name="uncheck_task"),
    path('check_task', views.check_task, name="check_task"),
    path('delete_timeline/<int:timeline_id>', views.delete_timeline, name='delete_timeline'),
    path('timeline/follow/<int:timeline_id>', views.followTimeline, name='follow_timeline'),
    path('timeline/unfollow/<int:timeline_id>', views.unfollowTimeline, name='unfollow_timeline'),
    # path('timeline/pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('timeline/pdf_view/<int:pk>', views.FooPDFView.as_view(), name="pdf_view"),
    path('timeline/pdf_download/<int:pk>', views.DownloadPDF.as_view(), name="pdf_download"),

    # タスクプロジェクト
    path('task_project/create/', views.TaskProject_CreateView.as_view(), name='TaskProject_Create'),
    path('task_project/detail/<int:pk>', views.TaskProject_DetailView.as_view(), name='TaskProject_Detail'),
    path('task_project/<int:pk>', views.TaskProject_ItemsView.as_view(), name='TaskProject_Items'),
    path('task_project/delete/<int:pk>', views.TaskProject_DeleteView.as_view(), name='TaskProject_Delete'),
    path('task_project/update/<int:pk>', views.TaskProject_UpdateView.as_view(), name='TaskProject_Update'),
    path('task_project/list/', views.TaskProject_ListView.as_view(), name='TaskProject_List'),
    path('delete_project/<int:project_id>', views.delete_project, name='delete_project'),
    path('project/follow/<int:project_id>', views.follow_project, name='follow_project'),
    path('project/unfollow/<int:project_id>', views.unfollow_project, name='unfollow_project'),

    # タスクセクション
    path('task_section/create/', views.TaskSection_CreateView.as_view(), name='TaskSection_Create'),
    path('task_section/detail/<int:pk>', views.TaskSection_DetailView.as_view(), name='TaskSection_Detail'),
    path('task_section/<int:pk>', views.TaskSection_ItemsView.as_view(), name='TaskSection_Items'),
    path('task_section/delete/<int:pk>', views.TaskSection_DeleteView.as_view(), name='TaskSection_Delete'),
    path('task_section/update/<int:pk>', views.TaskSection_UpdateView.as_view(), name='TaskSection_Update'),
    path('task_section/list/', views.TaskSection_ListView.as_view(), name='TaskSection_List'),

    # タスク
    path('task/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', views.TaskReorder.as_view(), name='task-reorder'),

]
