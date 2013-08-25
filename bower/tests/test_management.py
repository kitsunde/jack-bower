import os
from django.core.management import call_command
from django.test import TestCase


class BowerInitTest(TestCase):
    bower_files = [
        os.path.join(os.path.dirname(__file__),
                     'test_app',
                     bower_file) for bower_file in
        ['bower.json', '.bowerrc', '.gitignore']
    ]

    def tearDown(self):
        for bower_file in self.bower_files:
            os.remove(bower_file)

    def test_basic(self):
        call_command('bower_init', 'bower.tests.test_app')
        for bower_file in self.bower_files:
            self.assertTrue(os.path.exists(bower_file))
