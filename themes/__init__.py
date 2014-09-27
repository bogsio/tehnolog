__author__ = 'bogdan'

import os


class ThemeManager(object):

    @classmethod
    def _theme_names(cls):
        return [name for name in os.listdir(cls.theme_path())
                if os.path.isdir(os.path.join(cls.theme_path(), name))]

    @classmethod
    def theme_path(cls):
        return os.path.abspath(os.path.dirname(__file__))


class Theme(object):
    def __init__(self, theme_name):
        self.theme_name = theme_name