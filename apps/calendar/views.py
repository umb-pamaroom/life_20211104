import datetime
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import BS4ScheduleForm, SimpleScheduleForm
from .models import Schedule
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from . import mixins
from apps.app.models import *
from django.contrib.auth.models import User
from django.core import serializers
User = get_user_model()
import json


def update_task_title(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        note = Task.objects.get(pk=data["pk"])
        note.title = data["title"]
        note.save()
        print("下記のタスクのタイトルを更新しました")
        print(data["pk"])
        return JsonResponse({"message": "Success"})


def update_task_text(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        note = Task.objects.get(pk=data["pk"])
        note.description = data["description"]
        note.save()
        return JsonResponse({"message": "Success"})
    

def update_task_date(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        note = Task.objects.get(pk=data["pk"])
        note.date = data["date"]
        note.save()
        return JsonResponse({"message": "Success"})
    


def delete_task_calendar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        note = Task.objects.get(pk=data["pk"])
        note.deleted = True
        note.save()
        return JsonResponse({"message": "Success"})

def check_task_calendar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        # data["pk"]はhtmlの「data-pk」のこと
        print(data)
        checkbox = Task.objects.get(pk=data["pk"])
        checkbox.complete = True
        checkbox.save()
        return JsonResponse({"message": "Success"})


def uncheck_task_calendar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        checkbox = Task.objects.get(pk=data["pk"])
        checkbox.complete = False
        checkbox.save()
        return JsonResponse({"message": "Success"})
    

def show_task_calendar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        # data["pk"]はhtmlの「data-pk」のこと
        user = User.objects.get(pk=data["pk"])
        print(user.done_task_calendar_show)
        user.done_task_calendar_show = True
        user.save()
        return JsonResponse({"message": "Success"})


def unshow_task_calendar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.get(pk=data["pk"])
        print(user.done_task_calendar_show)
        user.done_task_calendar_show = False
        user.save()
        return JsonResponse({"message": "Success"})
    
# AJAXでカレンダーのタスクを作成する
def create_task_calendar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == "POST":
        data = json.loads(request.body)
        task = Task(title=data["title"], date=data["date"],user=request.user)
        task.save()
        print("タスクの作成成功")
        print(data["date"])
        print(task.pk)
        # クライアントにtaskのpkを渡す
        return JsonResponse({"message": "Success", "pk": task.pk})
    

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'calendar/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class WeekCalendar(mixins.WeekCalendarMixin, generic.TemplateView):
    """週間カレンダーを表示するビュー"""
    template_name = 'calendar/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class WeekWithScheduleCalendar(mixins.WeekWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの週間カレンダーを表示するビュー"""
    template_name = 'calendar/week_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class MonthWithScheduleCalendar(mixins.MonthWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'calendar/month_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'calendar/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('calendar:mycalendar', year=date.year, month=date.month, day=date.day)


class MonthWithFormsCalendar(mixins.MonthWithFormsMixin, generic.TemplateView):
    """フォーム付きの月間カレンダーを表示するビュー"""
    template_name = 'calendar/month_with_forms.html'
    model = Task
    context_object_name = 'tasks'
    date_field = 'date'
    form_class = SimpleScheduleForm

    # データを取得するメソッド
    def get(self, request, **kwargs):
        context = self.get_month_calendar()
        # 他のモデルをテンプレートで使いたい時はここに書く
        context['tasks'] = Task.objects.all().filter(user=self.request.user)
        return render(request, self.template_name, context)

    # データがpostで送られてきた時
    def post(self, request, **kwargs):
        context = self.get_month_calendar()
        formset = context['month_formset']
        if formset.is_valid():
            
            instances = formset.save(commit=False)
            for schedule in instances:
                # モデルはTask
                schedule.user = request.user
                schedule.save()

                # 更新した西暦の日付に戻す
                return redirect('calendar:month_with_forms', year=schedule.date.year, month=schedule.date.month)

        return render(request, self.template_name, context)

