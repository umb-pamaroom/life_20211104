from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('diary/', views.index, name='index'),

    # 自分の日報一覧
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
    path('timeline/list/', views.TimelineListView.as_view(), name='TimelineList'),

]
