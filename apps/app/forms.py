from django import forms
from django.forms import ModelForm
from .models import *
# タスクのフォーム


class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'section', 'title', 'description','date' ,'start_time','end_time','complete']

        # 時間を選択できるように
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'completed': forms.CheckboxInput(attrs={'class': 'check'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'section', 'title', 'description',
                  'date', 'start_time', 'end_time']

        # 時間を選択できるように
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'completed': forms.CheckboxInput(attrs={'class': 'check'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""

class PositionForm(forms.Form):
    position = forms.CharField()

class RoutineCreateForm(ModelForm):
    class Meta:
        model = RoutineModel
        fields = ['timeline', 'title', 'description', 'start_time', 'end_time', 'category','completed']
        labels = {
            'timeline': 'タイムライン',
            'completed': 'ステータス',
        }

        # 時間を選択できるように
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'completed': forms.CheckboxInput(attrs={'class': 'check'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


class TimelineCreateForm(ModelForm):
    class Meta:
        model = TimelineModel
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


class TimelineUpdateForm(ModelForm):
    class Meta:
        model = TimelineModel
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


# タイムラインの共有するフォーム
class TimelineShareForm(ModelForm):
    class Meta:
        model = TimelineModel
        fields = ['members']

        labels = {
            'members': '共有したいメンバーのメールアドレスにチェックを入れてください。',
        }
        widgets = {
            'members': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


"""""""""""""""""""""""""""""""""""""""""""""

プロジェクトのForm

▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

"""""""""""""""""""""""""""""""""""""""""""""


class TaskProject_CreateForm(ModelForm):
    class Meta:
        model = TaskProjectModel
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


class TaskProject_UpdateForm(ModelForm):
    class Meta:
        model = TaskProjectModel
        fields = ['title', 'description', 'members']

        labels = {
            'members': 'メンバー',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""


class TaskSection_CreateForm(ModelForm):
    class Meta:
        model = TaskSectionModel
        fields = ['project','title', 'description']
        labels = {
            'project': 'プロジェクト',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 「:」を削除
        self.label_suffix = ""

        

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
