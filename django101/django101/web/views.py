from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

# pure python func
# - called with django request object
# - returns django response
from django101.web.models import Todo, Category


def permissions_required(required_permissions):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated \
                    or not user.has_perms(required_permissions):
                return HttpResponse('No permission')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


# @login_required(login_url='/login-with-fb')
# @login_required
@permissions_required(required_permissions=['web.change_category'])
def index(request):
    if not request.user.is_authenticated:
        redirect('login')

    print(request.user)

    user = authenticate(
        request,
        username='doncho1',
        password='12345qwe',
    )

    # check whether user is in content_creator & content_manager
    # Change in admin requires new code
    # => "content reviewer"
    cat = Category.objects.get(pk=4)
    cat.name = 'New Name 2'
    cat.save()

    if user:
        login(request, user)

    context = {
        'title': 'Function-based view',
    }

    return render(request, 'index.html', context)


class IndexView(LoginRequiredMixin, views.View):
    def get(self, request):
        context = {
            'title': 'Class-based view',
        }

        return render(request, 'index.html', context)

    def dispatch(self, request, *args, **kwargs):
        # custom logic
        return super().dispatch(request, *args, **kwargs)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'
        return context


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My todos'

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)

        return queryset


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'todo-details.html'
    context_object_name = 'todo'

    # def get_object(self, queryset=None):

    # def get_template_names(self):
    #     # if admin => show admin template
    #     # else => show regular template


class CreateTodoForm:
    pass


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')  # When the same for each create
    fields = ('title', 'description', 'category')

    # form_class = CreateTodoForm

    # def get_form_class(self):
    #     pass

    # When different based on the create
    # def get_success_url(self):
    #     pass

# def sample():
#     pk = 1
#     Todo.objects.get(pk=pk)
#     Todo.objects.filter(pk=pk).get()

# class RedirectToIndexView(views.RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         if ...:
#             return 'place 1'
#         else:
#             return 'place 2'

# class PetDetails(views.DetailView):
#     model = Pet # The model
#     template_name = 'pet-details.html'
