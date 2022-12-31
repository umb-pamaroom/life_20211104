from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("スーパーユーザーテスト")
        User.objects.create_superuser(
            email=settings.SUPERUSER_EMAIL,
            password=settings.SUPERUSER_PASSWORD
        )
        print(settings.SUPERUSER_EMAIL)
        print(settings.SUPERUSER_PASSWORD)
