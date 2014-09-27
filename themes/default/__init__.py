__author__ = 'bogdan'

from themes import BaseTheme


class Theme(BaseTheme):
    PAGES = {
        ## Admin pages
        'admin_index': 'admin_index.html',
        'admin_login': 'admin_login.html',

        ## Blog pages
        'index': 'index.html',
    }

