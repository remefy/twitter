from django.contrib.admin import site

from blog.models import Tweeter

site.register(Tweeter)
