import os
import pkgutil
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            path = pkgutil.get_loader(app).filename
            if os.path.exists(os.path.join(path, 'bower.json')):
                os.chdir(path)
                os.system('bower install')