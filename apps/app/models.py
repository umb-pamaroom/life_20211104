import datetime
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

# 選択肢用のクラス
class MealAllEval(models.TextChoices):
    VEGETABLE = '野菜が少ない', '野菜が少ない'
    CALORIE = 'カロリーが高い', 'カロリーが高い'
    NUTRITION = '栄養満点', '栄養満点'


class RoutineCategory(models.TextChoices):
    INBOX = 'インボックス', 'インボックス'
    LIFE = '生活', '生活'
    WORK = '仕事', '仕事'
    FAMILY = '家族', '家族'


class RoutineStatus(models.TextChoices):
    PASSED = '過ぎています。', '過ぎています。'
    COMPLETE = '完了', '完了'
    NOW = '対応中', '対応中'
    YET = '未対応', '未対応'

# 選択肢用のクラス
class Condition(models.TextChoices):
    GOOD = '良好', '良好'
    USUALLY = '普通', '普通'
    UPSET = '悪い', '悪い'


# ルーティーンのモデル
class RoutineModel(models.Model):
    create_user = models.ForeignKey(User, related_name='relate_user_routine', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('タイトル', max_length=50)
    description = models.TextField('説明', blank=True)
    start_time = models.TimeField('開始時間')
    end_time = models.TimeField('終了時間' ,blank=True , null=True)
    category = models.CharField('カテゴリ', max_length=30, blank=True, default='インボックス', choices=RoutineCategory.choices)
    status = models.CharField('ステータス', max_length=30, blank=True, default='未対応', choices=RoutineStatus.choices)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


# Memoモデルを作成する
class Memo(models.Model):

    create_user = models.ForeignKey(User, related_name='relate_user', on_delete=models.CASCADE, null=True, blank=True)

    # 日付
    dateData = models.DateField(default=timezone.now, blank=True)
    discovery = models.TextField(blank=True)
    tired = models.TextField(blank=True)
    dislike = models.TextField(blank=True)
    happy = models.TextField(blank=True)
    best = models.TextField(blank=True)
    tomorrow = models.TextField(blank=True)
    other = models.TextField(blank=True)
    summarize = models.TextField(blank=True)

    breakfast = models.ImageField(upload_to='images/breakfast/%Y/%m/%d/%s/', blank=True, null=True)

    # 朝食名
    breakfastName = models.CharField(max_length=30, blank=True)

    lunch = models.ImageField(upload_to='images/lunch/%Y/%m/%d/%s/', blank=True, null=True)

    lunchName = models.CharField(max_length=30, blank=True)

    dinner = models.ImageField(upload_to='images/dinner/%Y/%m/%d/%s/', blank=True, null=True)

    dinnerName = models.CharField(max_length=30, blank=True)

    snack = models.ImageField(upload_to='images/snack/%Y/%m/%d/%s/', blank=True, null=True)

    snackName = models.CharField(max_length=30, blank=True)

    # 食事の総合評価
    mealEvaluation = models.CharField(max_length=30, blank=True, default='', choices=MealAllEval.choices)

    # 食事へのコメント
    mealComment = models.TextField(blank=True)

    # 体調
    condition = models.CharField(max_length=30, blank=True, default='', choices=Condition.choices)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.discovery


    
