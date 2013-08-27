from collections import OrderedDict
import json
import os
from django.core.management import CommandError
from bower.management.base import AppDirectoryCommand
from django.conf import settings

BOWER_INSTALL = getattr(settings, 'BOWER_INSTALL', "bower install")

print BOWER_INSTALL


class Command(AppDirectoryCommand):
    def handle_app(self, app_path):
        bower_file = os.path.join(app_path, 'bower.json')
        package_name = os.path.basename(app_path)

        if os.path.exists(bower_file):
            with open(bower_file, "r+") as bower_fp:
                # Version <1.0 didn't require a package name. We'll need to
                # upgrade those packages. We need an ordered dict so we don't
                # re-arrange the keys.
                bower_package = json.load(bower_fp,
                                          object_pairs_hook=OrderedDict)
                if not 'name' in bower_package:
                    print "Bower 1.0 requires a package name, " \
                          "adding for %s" % package_name
                    # We'll put the name first because it looks better.
                    bower_package = OrderedDict({'name': package_name},
                                                **bower_package)
                    bower_fp.seek(0)
                    bower_fp.truncate()
                    # Prevent json.dump to add a space after ,
                    json.dump(bower_package, bower_fp, indent=4,
                              separators=(',', ': '))

            os.chdir(app_path)

            if os.system(BOWER_INSTALL) != 0:
                raise CommandError("Bower encountered an issue while "
                                   "installing.")
