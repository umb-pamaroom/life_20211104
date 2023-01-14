from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from apps.app.models import *

# 選択肢用のクラス
class Themes(models.TextChoices):
    WHITE = 'white', 'ホワイト'
    DARK = 'dark', 'ダーク'

# カテゴリ表示・非表示選択肢用のクラス
class TimelineSettingsCategoryShow(models.TextChoices):
    SHOW = 'show', '表示'
    NONE = 'none', '非表示'


class CustomUserManager(UserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル

    usernameを使わず、emailアドレスをユーザー名として使うようにしています。

    """
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    introduction = models.TextField(_('introduction'), max_length=150, blank=True)

    # お気に入りタイムライン
    favorite_timeline = models.ManyToManyField(TimelineModel, related_name='favorite_timeline', verbose_name='お気に入りのタイムライン', blank=True)

    favorite_project = models.ManyToManyField(TaskProjectModel, related_name='favorite_project', verbose_name='お気に入りのプロジェクト', blank=True)

    # プロフィール画像
    avatar = models.ImageField('プロフィール画像',upload_to='images/avatar', blank=True, null=True)

    # カレンダーのタスク表示・非表示設定
    done_task_calendar_show = models.BooleanField(default=False)

    # 選択肢用をchoicesで追加する
    theme = models.CharField(max_length=30, default="white", choices=Themes.choices)
    timeline_settings_category_show = models.CharField(max_length=30, default="show", choices=TimelineSettingsCategoryShow.choices)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # def get_full_name(self):
    #     """Return the name plus the introduction, with a space in
    #     between."""
    #     full_name = '%s %s' % (self.name, self.introduction)
    #     return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email
