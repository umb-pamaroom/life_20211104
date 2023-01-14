from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('calendar', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('week/', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendar.as_view(), name='week'),
    path('week_with_schedule/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
    path(
        'week_with_schedule/<int:year>/<int:month>/<int:day>/',
        views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'
    ),
    # 現在の日付に合わせた月のカレンダーが表示される
    path(
        'month_with_schedule/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    # セレクトした月のカレンダーが表示される
    path(
        'month_with_schedule/<int:year>/<int:month>/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
    ),
    path(
        'month_with_forms/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path(
        'month_with_forms/<int:year>/<int:month>/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),

    path('uncheck_task_calendar', views.uncheck_task_calendar, name="uncheck_task_calendar"),
    path('check_task_calendar', views.check_task_calendar, name="check_task_calendar"),
    path('unshow_task_calendar', views.unshow_task_calendar, name="unshow_task_calendar"),
    path('show_task_calendar', views.show_task_calendar, name="show_task_calendar"),
    path('create_task_calendar', views.create_task_calendar, name="create_task_calendar"),
    path('delete_task_calendar', views.delete_task_calendar, name="delete_task_calendar"),

    path('update_task_title', views.update_task_title, name="update_task_title"),
    path('update_task_text', views.update_task_text, name="update_task_text"),
    path('update_task_date', views.update_task_date, name="update_task_date"),
    
]
