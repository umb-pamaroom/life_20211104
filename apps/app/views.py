from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Memo, RoutineModel
#ListViewのインポート
from django.views.generic.list import ListView
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from .forms import MemoForm, RoutineCreateForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect


class RoutineCreateView(LoginRequiredMixin, CreateView):
    template_name = 'routine/create.html'
    model = RoutineModel

    # forms.pyで定義したクラスを使う
    form_class = RoutineCreateForm

    success_url = reverse_lazy('app:RoutineList')
    
    def form_valid(self, form):
        # form.instance.created_user = self.request.user
        # return super().form_valid(form)
        # viewsで直接、ユーザを入力している
        obj = form.save(commit=False)
        obj.create_user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('app:RoutineList'))

    # 「RoutineList」はurls.pyのname


class RoutineUpdateView(UpdateView):
    template_name = 'routine/update.html'
    model = RoutineModel

    form_class = RoutineCreateForm

    def get_success_url(self):
        return reverse('app:RoutineDetail', kwargs={'pk': self.object.pk})



class RoutineDetailView(LoginRequiredMixin, DetailView):
    template_name = 'routine/detail.html'
    model = RoutineModel

    context_object_name = 'routines'


class RoutineDeleteView(DeleteView):
    template_name = 'routine/delete.html'
    model = RoutineModel
    context_object_name = 'routines'

    success_url = reverse_lazy('app:RoutineList')


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
