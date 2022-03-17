from django.urls import reverse
from django.views import generic as views

from testing_demos.web.models import Profile


class ProfileCreateView(views.CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/create.html'

    def get_success_url(self):
        return reverse('details profile', kwargs={'pk': self.object.pk})


class ProfilesListView(views.ListView):
    model = Profile
    template_name = 'profiles/list.html'
    context_user_key = 'user'
    no_logged_in_user_value = 'No user'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            context[self.context_user_key] = self.request.user.username
        else:
            context[self.context_user_key] = self.no_logged_in_user_value

        return context

    # def get_queryset(self):
    #     return super().get_queryset() \
    #         .prefetch_related('') \
    #         .filter()


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/details.html'
