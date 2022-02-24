from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User

# 管理画面でデータをインポート・エクスポート
from import_export import resources
from import_export.admin import ImportExportMixin


class UserResource(resources.ModelResource):
    class Meta:
        model = User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserAdmin(ImportExportMixin, UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
         'fields': ('name', 'introduction', 'theme','favorite_timeline', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'name', 'introduction',
                    'is_staff', 'theme', 'avatar')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name', 'introduction', 'theme','favorite_timeline', 'avatar')
    ordering = ('email',)
    resource_class = UserResource


class UserThemeAdmin(admin.ModelAdmin):
    fields = ['color']

admin.site.register(User, MyUserAdmin)

