import os
from bower.management.base import AppDirectoryCommand
import shutil


class Command(AppDirectoryCommand):
    default_apps = None

    def handle_app(self, app_path):
        init_files = os.path.join(os.path.dirname(__file__), "../init_files")
        for init_file in os.listdir(init_files):
            target_file = os.path.join(app_path, init_file)

            if not os.path.exists(target_file):
                shutil.copyfile(os.path.join(init_files, init_file),
                                target_file)

        print "Add your dependencies to %s " % os.path.join(app_path,
                                                            'bower.json')