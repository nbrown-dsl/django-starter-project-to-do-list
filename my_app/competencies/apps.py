from django.apps import AppConfig


class CompetenciesConfig(AppConfig):
    name = 'competencies'

    def ready(self):
        import competencies.signals
