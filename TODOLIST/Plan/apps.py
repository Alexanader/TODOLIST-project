from django.apps import AppConfig


class PlantodoAppConfig(AppConfig):
    name = 'Plan'
    verbose_name = 'Plan base'

    def ready(self):
    	from Plan import signals
