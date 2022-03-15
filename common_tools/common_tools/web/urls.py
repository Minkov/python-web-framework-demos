from django.urls import path

from common_tools.web.views import show_index, ProfilesListView

urlpatterns = (
    path('', show_index, name='index'),
    path('profiles/', ProfilesListView.as_view(), name='profiles list'),
)

import common_tools.web.signals
