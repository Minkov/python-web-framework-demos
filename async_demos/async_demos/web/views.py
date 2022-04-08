import time

from django import views
from django.http import JsonResponse

from async_demos.web.tasks import slow_task


class SlowTaskView(views.View):
    def get(self, request, is_slow):
        start = time.time()
        if is_slow:
            slow_task(15)
        else:
            slow_task.delay(15)
        end = time.time()
        return JsonResponse(data={
            'time_executed': end - start,
        })
