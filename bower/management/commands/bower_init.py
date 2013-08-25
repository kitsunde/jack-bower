import os
from django.template import Template, Context
from bower.management.base import AppDirectoryCommand


class Command(AppDirectoryCommand):
    default_apps = None

    def handle_app(self, app_path):
        init_files = os.path.join(os.path.dirname(__file__), "../init_files")
        for init_file in os.listdir(init_files):
            target_file = os.path.join(app_path, init_file)

            if not os.path.exists(target_file):
                with open(os.path.join(init_files, init_file)) as template_file:
                    template = Template(template_file.read())
                context = Context({
                    'app_name': os.path.basename(app_path)
                })
                with open(os.path.join(app_path, init_file), "w") as f:
                    f.write(template.render(context))

        print "Add your dependencies to %s " % os.path.join(app_path,
                                                            'bower.json')
