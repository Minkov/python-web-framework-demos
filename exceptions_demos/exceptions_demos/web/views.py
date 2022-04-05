from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Model
from django.http import HttpResponse, Http404
from django import views

from exceptions_demos.web.models import Todo, Category


class AppException(Exception):
    pass


class MyView(LoginRequiredMixin, views.View):
    login_url = 'URL FOR THIS VIEW ONLY'

    def get(self, request):
        return HttpResponse('It works')


def raises_exception():
    # raise AppException('Object has invalid Id. Valid IDs are 1, 2, 3, 7')
    raise Http404('Not found my object')


def raises_exception_view(request):
    todos = list(Todo.objects.all())
    for todo in todos:
        print(todo)
    raises_exception()


def get_or_create_category(name):
    try:
        return Category.objects.get(name=name)
    except Model.DoesNotExist:
        return Category.objects.create(name=name)


def create_todo(request):
    category_name = request.POST.get('category')

    category = get_or_create_category(category_name)


def todo_by_id(pk):
    # Variant 1, the way
    try:
        todo = Todo.objects.get(pk=pk)
    except Model.DoesNotExist:
        # Handle does not exist => show 404
        pass

    # Variant 2, without exceptions
    todo = Todo.objects.filter(pk=pk)
    if not todo:
        # Handle does not exist => show 404
        pass


def internal_error(request):
    return HttpResponse('An error occurred, please try again')


class InternalErrorView(views.View):
    def get(self, request):
        return HttpResponse('An error occurred, please try again. (CBV)')
