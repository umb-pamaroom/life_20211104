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

# 選択肢用のクラス
class Condition(models.TextChoices):
    GOOD = '良好', '良好'
    USUALLY = '普通', '普通'
    UPSET = '悪い', '悪い'


# Memoモデルを作成する
class Memo(models.Model):

    create_user = models.ForeignKey(User, related_name='relate_user', on_delete=models.CASCADE, null=True, blank=True)

    # 日付
    dateData = models.DateField(default=timezone.now, blank=True)

    # 学んだこと
    discovery = models.TextField(blank=True)

    # 学んだこと
    tired = models.TextField(blank=True)

    # 学んだこと
    dislike = models.TextField(blank=True)

    # 学んだこと
    happy = models.TextField(blank=True)

    # 学んだこと
    best = models.TextField(blank=True)

    # 学んだこと
    tomorrow = models.TextField(blank=True)

    # 学んだこと
    other = models.TextField(blank=True)

    # 学んだこと
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


    
