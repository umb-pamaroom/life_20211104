from django.shortcuts import render, redirect
from .models import Memo
#ListViewのインポート
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .forms import MemoForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

@login_required
def index(request):

  # 投稿の並び順を制御する
  memos = Memo.objects.all().order_by('-dateData')
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
  memos = Memo.objects.all().order_by('-dateData')
  keyword = request.GET.get('keyword')

  if keyword:
      memos = memos.filter(
          Q(discovery__icontains=keyword)
      )
      messages.success(request, '「{}」の検索結果'.format(keyword))
  return render(request, 'app/mydiary.html', {'memos': memos})


# class MydiaryListView(ListView):
#     template_name = 'app/mydiary.html'
#     model = Memo

#     def get_queryset(self):
#         return self.model.objects.filter(
#             create_user=self.request.user,
#         )


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
