import time

from celery import shared_task


@shared_task
def slow_task(n):
    result = 0
    for i in range(n):
        time.sleep(1)
        result += i
    print(result)
