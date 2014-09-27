__author__ = 'bogdan'

import os
import importlib


class ThemeManager(object):

    @classmethod
    def _theme_names(cls):
        return [name for name in os.listdir(cls.theme_path())
                if os.path.isdir(os.path.join(cls.theme_path(), name))]

    @classmethod
    def theme_path(cls):
        return os.path.abspath(os.path.dirname(__file__))

    @classmethod
    def get_theme(cls, theme_name):
        ThemeModule = importlib.import_module('themes.' + theme_name)
        return ThemeModule.Theme(theme_name)


class Theme(object):

    PAGES = {
        'index': 'index.html',
    }

    def __init__(self, theme_name):
        self.theme_name = theme_name

    def template_folder(self):
        return os.path.join(os.path.join(self.theme_name), 'templates')

    def get_template(self, page='index'):
        return os.path.join(os.path.join(self.template_folder(), self.PAGES[page]))