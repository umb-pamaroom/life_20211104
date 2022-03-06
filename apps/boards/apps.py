from django.apps import AppConfig


class BoardsConfig(AppConfig):
    name = 'apps.boards'

    def ready(self):
    	import apps.boards.signals