from django.urls import path

from async_demos.web.views import SlowTaskView

urlpatterns = (
    path('<int:is_slow>/', SlowTaskView.as_view(), name='slow view'),
)
