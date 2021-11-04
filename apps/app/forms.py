from django.forms import ModelForm
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['create_user', 'dateData', 'discovery', 'tired', 'happy', 'best', 'tomorrow', 'dislike','other', 'summarize', 'breakfast', 'breakfastName', 'lunch','lunchName', 'dinner', 'dinnerName' , 'snack', 'snackName', 'mealEvaluation', 'mealComment', 'condition']
        labels = {
            'dateData': '日付',
            'discovery': '学んだこと',
            'tired': '印象に残ったこと',
            'dislike': '改善点',
            'happy': '嬉しかったこと',
            'best': '頑張ったこと',
            'tomorrow': '明日したいこと',
            'other': 'その他',
            'summarize': '1日のまとめ',
            'breakfast': '朝食',
            'breakfastName': '朝食名',
            'lunch': '昼食',
            'lunchName': '昼食名',
            'dinner': '夕食',
            'dinnerName': '夕食名',
            'snack': '間食',
            'snackName': '間食名',
            'mealEvaluation': '食事の総合評価',
            'mealComment': '食事へのコメント',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""
