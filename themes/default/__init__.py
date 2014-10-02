__author__ = 'bogdan'

from themes import BaseTheme


class Theme(BaseTheme):
    PAGES = {
        ## Admin pages
        'admin_index': 'admin_index.html',
        'admin_login': 'admin_login.html',
        'admin_add_post': 'admin_add_post.html',
        'admin_detail_post': 'admin_detail_post.html',
        'admin_categories': 'admin_categories.html',
        ## Blog pages
        'index': 'index.html',
    }

