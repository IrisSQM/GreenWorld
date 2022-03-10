from __future__ import unicode_literals
import os

AUTHOR = 'Iris'
SITENAME = 'Green World'
SITEURL = ''

# Content paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blogs']

# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.png'

# Social widget
SOCIAL = (
  ('Github', 'https://github.com/IrisSQM'),
  ('Facebook', 'https://www.facebook.com/QimengShi17'),
  ('Instagram', 'https://www.instagram.com/qimengshi/')
)

# Home Content
HERO = [
  {
    'image': '/images/home/fishes.jpg',
    # for multilanguage support, create a simple dict
    'title': 'Green World',
    'text': 'This is a place for seeking pleasures beyond the hustle and bustle of daily life. Sincerely designed and maintained by Iris.',
    'links': [
        {
        'icon': 'icon-code',
        'url': 'https://www.metmuseum.org/art/collection/search/40393',
        'text': 'Learn about the background painting'
      }]
  }, {
    'image': '/images/home/grad.jpeg',
    # keep it a string if you dont need multiple languages
    'title': '绿色世界',
    # keep it a string if you dont need multiple languages
    'text': '欢迎来到社恐Iris的“绿色世界”！绿色世界是莎士比亚戏剧中颠覆常规的地方，希望在这里你能发现物外之乐。我不营销内容，我创造快乐。',
    'links': []
  }, {
    'image': '/images/home/haori.jpg',
    'title': '日日是好日',
    'text': '如何把平常日子过得不平凡？记住日日是好日。',
    'links': []
  }
]


ABOUT = {
  'image': '/images/about/about.jpeg',
  'mail': 'shiqimeng_1@163.com',
  # keep it a string if you dont need multiple languages
  'text': 'If you have any questions and would like a further discussion, please contact me through email.'
}

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = 'themes/pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = 'themes/pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html'),
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'contact' # needed for the contact form
]




