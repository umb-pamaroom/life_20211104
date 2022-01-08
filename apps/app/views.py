from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Memo, RoutineModel, TimelineModel, Task, TaskProjectModel, TaskSectionModel
#ListViewのインポート
from django.views.generic.list import ListView
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .forms import MemoForm, RoutineCreateForm, TimelineCreateForm, PositionForm, TaskProject_CreateForm, TaskSection_CreateForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.db import transaction
from django.views import View


"""""""""""""""""""""""""""""""""""""""""""""

タスクのView

▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

"""""""""""""""""""""""""""""""""""""""""""""

class TaskList(LoginRequiredMixin, ListView):
    template_name = 'task/task_list.html'
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    template_name = 'task/task.html'
    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    template_name = 'task/task_form.html'
    model = Task
    fields = ['section', 'title', 'description', 'complete']
    success_url = reverse_lazy('app:tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'task/task_form.html'
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('app:tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'task/task_confirm_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('app:tasks')

    # 下記があると、タイムラインの削除でエラーが出る
    # def get_queryset(self):
    #     owner = self.request.user
    #     return self.model.objects.filter(user=owner)


class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('app:tasks'))





"""""""""""""""""""""""""""""""""""""""""""""

プロジェクトのView

▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

"""""""""""""""""""""""""""""""""""""""""""""


class TaskProject_CreateView(LoginRequiredMixin, CreateView):
    template_name = 'task_project/create.html'
    model = TaskProjectModel
    form_class = TaskProject_CreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.create_user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('app:TaskProject_List'))


class TaskProject_UpdateView(UpdateView):
    template_name = 'task_project/update.html'
    model = TaskProjectModel

    form_class = TaskProject_CreateForm

    def get_success_url(self):
        return reverse('app:TaskProject_Detail', kwargs={'pk': self.object.pk})


class TaskProject_DetailView(LoginRequiredMixin, DetailView):
    template_name = 'task_project/detail.html'
    model = TaskProjectModel
    context_object_name = 'TaskProject_object'


# タスクプロジェクトのタイトルと、そのプロジェクトセクションを表示
class TaskProject_ItemsView(LoginRequiredMixin, DetailView):
    template_name = 'task_project/items.html'
    model = TaskProjectModel
    context_object_name = 'TaskProject_object'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter(
            create_user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 「TaskSectionModel」モデルのprojectとそのプロジェクトが等しいものを代入
        context['task_section_items'] = TaskSectionModel.objects.all().filter(project=self.kwargs['pk'])
        return context


class TaskProject_DeleteView(DeleteView):
    template_name = 'task_project/delete.html'
    model = TaskProjectModel
    context_object_name = 'TaskProject_object'

    success_url = reverse_lazy('app:TaskProject_List')


class TaskProject_ListView(LoginRequiredMixin, ListView):
    template_name = 'task_project/list.html'
    model = TaskProjectModel
    context_object_name = 'TaskProject_object'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter(create_user=self.request.user).order_by('-updated_datetime', '-created_datetime')

        return queryset

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


"""""""""""""""""""""""""""""""""""""""""""""

▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

タスクプロジェクトのView
タスクセクションをまとめるもの

"""""""""""""""""""""""""""""""""""""""""""""




"""""""""""""""""""""""""""""""""""""""""""""

タスクセクションのView
タスクセクションをまとめるもの
メインモデル:TaskSectionModel
使用フォーム:TaskSection_CreateForm

▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

"""""""""""""""""""""""""""""""""""""""""""""


class TaskSection_CreateView(LoginRequiredMixin, CreateView):
    template_name = 'task_section/create.html'
    model = TaskSectionModel
    form_class = TaskSection_CreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.create_user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('app:TaskSection_List'))


class TaskSection_UpdateView(UpdateView):
    template_name = 'task_section/update.html'
    model = TaskSectionModel

    form_class = TaskSection_CreateForm

    def get_success_url(self):
        return reverse('app:TaskSection_Detail', kwargs={'pk': self.object.pk})


class TaskSection_DetailView(LoginRequiredMixin, DetailView):
    template_name = 'task_section/detail.html'
    model = TaskSectionModel
    context_object_name = 'TaskSection_object'


# タスクセクションのタイトルと、、そのセクションのタスクを表示
class TaskSection_ItemsView(LoginRequiredMixin, DetailView):
    template_name = 'task_section/items.html'
    model = TaskSectionModel
    context_object_name = 'TaskSection_object'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        queryset = queryset.filter(
            create_user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # task_itemsコンテキストに、､検索して一致するものを代入する
        # 代入するものは、そのセクションのタスク！
        # sectionとself.kwargs['pk']が等しいもの！ sectionの部分のものは、foreignkkeyのもの
        context['task_items'] = Task.objects.all().filter(section=self.kwargs['pk'])
        return context


class TaskSection_DeleteView(DeleteView):
    template_name = 'task_section/delete.html'
    model = TaskSectionModel
    context_object_name = 'TaskSection_object'

    success_url = reverse_lazy('app:TaskSection_List')


class TaskSection_ListView(LoginRequiredMixin, ListView):
    template_name = 'task_section/list.html'
    model = TaskSectionModel
    context_object_name = 'TaskSection_object'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter(
            create_user=self.request.user).order_by('-updated_datetime', '-created_datetime')

        return queryset


"""""""""""""""""""""""""""""""""""""""""""""

▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲

タスクセクションのView
タスクセクションをまとめるもの

"""""""""""""""""""""""""""""""""""""""""""""




# タイムラインのView
class TimelineCreateView(LoginRequiredMixin, CreateView):
    template_name = 'timeline/create.html'
    model = TimelineModel
    form_class = TimelineCreateForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.create_user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('app:TimelineList'))


class TimelineUpdateView(UpdateView):
    template_name = 'timeline/update.html'
    model = TimelineModel

    form_class = TimelineCreateForm

    def get_success_url(self):
        # return reverse('app:TimelineDetail', kwargs={'pk': self.object.pk})
        return reverse('app:TimelineList')


class TimelineDetailView(LoginRequiredMixin, DetailView):
    template_name = 'timeline/detail.html'
    model = TimelineModel
    context_object_name = 'timelines'


# タイムラインのタイトルと、タイムラインの項目を表示
class TimelineItemsView(LoginRequiredMixin, DetailView):
    template_name = 'timeline/items.html'
    model = TimelineModel
    context_object_name = 'timelines'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter(
            create_user=self.request.user)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # timeline_itemsコンテキストに「RoutineModel」の全てから検索して、モデルのtimeline項目がself.kwargs.pkに一致するもの
        context['timeline_items'] = RoutineModel.objects.all().filter(timeline=self.kwargs['pk']).order_by('start_time')
        return context


class TimelineDeleteView(DeleteView):
    template_name = 'timeline/delete.html'
    model = TimelineModel
    context_object_name = 'timelines'

    success_url = reverse_lazy('app:TimelineList')


class TimelineListView(LoginRequiredMixin, ListView):
    template_name = 'timeline/list.html'
    model = TimelineModel
    context_object_name = 'timelines'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter(
            create_user=self.request.user).order_by('-updated_datetime', '-created_datetime')

        return queryset





"""""""""""""""""""""""""""""""""""""""""""""

ルーティーンのView
メインモデル:
使用フォーム:

▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

"""""""""""""""""""""""""""""""""""""""""""""

class RoutineCreateView(LoginRequiredMixin, CreateView):
    template_name = 'routine/create.html'
    model = RoutineModel

    # forms.pyで定義したクラスを使う
    form_class = RoutineCreateForm
    
    def form_valid(self, form):
        # form.instance.created_user = self.request.user
        # return super().form_valid(form)
        # viewsで直接、ユーザを入力している
        obj = form.save(commit=False)
        obj.create_user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('app:TimelineList'))



class RoutineUpdateView(UpdateView):
    template_name = 'routine/update.html'
    model = RoutineModel

    form_class = RoutineCreateForm
    context_object_name = 'routines'

    def get_success_url(self):
        # return reverse('app:RoutineDetail', kwargs={'pk': self.object.pk})
        return reverse('app:TimelineList')


class RoutineDetailView(LoginRequiredMixin, DetailView):
    template_name = 'routine/detail.html'
    model = RoutineModel

    context_object_name = 'routines'


class RoutineDeleteView(DeleteView):
    template_name = 'routine/delete.html'
    model = RoutineModel
    context_object_name = 'routines'

    success_url = reverse_lazy('app:TimelineList')


class RoutineListView(LoginRequiredMixin, ListView):
    template_name = 'routine/list.html'
    model = RoutineModel
    # ordering = '-start_time'
    context_object_name = 'routines'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        # is_publishedがTrueのものに絞り、titleをキーに並び変える
        queryset = queryset.filter(create_user=self.request.user).order_by('start_time')

        return queryset



@login_required
def index(request):

  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData', '-updated_datetime' , '-created_datetime')
  keyword = request.GET.get('keyword')

  if keyword:
      memos = memos.filter(
          Q(discovery__icontains=keyword)
      )
      messages.success(request, '「{}」の検索結果'.format(keyword))
  return render(request, 'app/index.html', {'memos': memos})


@login_required
def mydiary(request):

  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData', '-updated_datetime', '-created_datetime')
  keyword = request.GET.get('keyword')

  if keyword:
      memos = memos.filter(
          Q(discovery__icontains=keyword)
      )
      messages.success(request, '「{}」の検索結果'.format(keyword))
  return render(request, 'app/mydiary.html', {'memos': memos})


@login_required
def detail(request, memo_id):
  # プライマリキーをmemo_idにする
  memo = get_object_or_404(Memo, id=memo_id)
  return render(request, 'app/detail.html', {'memo': memo})

@login_required
def new_memo(request):
  return render(request, 'app/new_memo.html')


@login_required
def new_memo(request):
    form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form})


@login_required
def new_memo(request):
    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES)

        qryset = form.save()
        qryset.create_user = request.user
        if form.is_valid():
            qryset.save()
            return redirect('app:index')
    else:
        form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form})


@login_required
def meal_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  keyword = request.GET.get('keyword')

  if keyword:
      memos = memos.filter(
          Q(breakfastName__icontains=keyword) | Q(lunchName__icontains=keyword) | Q(dinnerName__icontains=keyword)
      )
      messages.success(request, '「{}」の検索結果'.format(keyword))

  return render(request, 'app/meal_list.html', {'memos': memos})


@login_required
def breakfast_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/breakfast_list.html', {'memos': memos})


@login_required
def lunch_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/lunch_list.html', {'memos': memos})


@login_required
def dinner_list(request):
  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
  return render(request, 'app/dinner_list.html', {'memos': memos})


@login_required
@require_POST
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('app:index')


@login_required
def edit_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'app/edit_memo.html', {'form': form, 'memo': memo})
