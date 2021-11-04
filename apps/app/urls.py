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
]
