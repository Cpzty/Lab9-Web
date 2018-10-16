from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_pattern
from .views import CreateView

urlpatterns = {
    url(r'^chismes/$', CreateView.as_view(), name="create"),
    }

url patterns = format_suffix_patterns(urlpatterns)
