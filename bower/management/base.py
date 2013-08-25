import pkgutil
from django.conf import settings
from django.core.management import BaseCommand, CommandError


class AppDirectoryCommand(BaseCommand):
    """
    Takes one or more installed application names as arguments, and does
    something with each of them.

    Rather than implementing ``handle()``, subclasses must implement
    ``handle_app()``, which will be called once for each application.
    """
    args = '<appname appname ...>'
    default_apps = settings.INSTALLED_APPS
    requires_model_validation = False

    def handle(self, *app_labels, **options):
        if not app_labels:
            if self.default_apps:
                app_labels = self.default_apps
            else:
                raise CommandError('Enter at least one appname.')

        for app_label in set(app_labels) - set(settings.INSTALLED_APPS):
            raise CommandError("%s not found in INSTALLED_APPS" % app_label)

        for app in app_labels:
            path = pkgutil.get_loader(app).filename
            self.handle_app(path)

    def handle_app(self, app_label):
        raise NotImplementedError()
