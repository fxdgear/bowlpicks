import os
import sys
import site

PROJECT_ROOT = '/home/nick/code/python/bowlpicks/src/bowlpicks/bowlpicks'
site_packages = '/home/nick/code/python/bowlpicks/lib/python2.6/site-packages'

site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(1, os.path.join(PROJECT_ROOT))
sys.path.insert(2, site_packages)
os.environ['DJANGO_SETTINGS_MODULE'] = 'bowlpicks.settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/administrator/.python-eggs'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
