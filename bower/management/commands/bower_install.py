import os
from django.core.management import CommandError
from bower.management.base import AppDirectoryCommand


class Command(AppDirectoryCommand):
    def handle_app(self, app_path):
        if os.path.exists(os.path.join(app_path, 'bower.json')):
            os.chdir(app_path)
            if os.system('bower install') != 0:
                raise CommandError("Bower encountered an issue while "
                                   "installing.")