import os
from bower.management.base import AppDirectoryCommand


class Command(AppDirectoryCommand):
    def handle_app(self, app_path):
        if os.path.exists(os.path.join(app_path, 'bower.json')):
            os.chdir(app_path)
            os.system('bower install')