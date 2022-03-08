from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from auth_demos.auth_app.models import Profile

UserModel = get_user_model()


class RestrictedView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'index.html'


class UserRegistrationForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(max_length=25)

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            **self.cleaned_data,
            user=user,
        )
        if commit:
            profile.save()

        return user


class UserRegistrationView(views.CreateView):
    # form_class = auth_forms.UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    pass
