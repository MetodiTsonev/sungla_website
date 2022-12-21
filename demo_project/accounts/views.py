from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from demo_project.accounts.forms import UserRegisterForm, LoginForm, ProfileEditForm, UserModel
from demo_project.accounts.models import AppUser


class SignOutView(LogoutView):
    next_page = reverse_lazy('login user')


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'account_temp/login-page.html'
    next_page = reverse_lazy('index')


class SignUpView(CreateView):
    template_name = 'account_temp/register-page.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class ProfileDetailsView(DetailView):
    template_name = 'account_temp/profile-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        return context


class ProfileEditView(UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'account_temp/edit-page.html'

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.request.user.pk,
        })


class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = 'account_temp/profile-delete-page.html'
    next_page = reverse_lazy('index')

    def post(self, *args, pk):
        self.request.user.delete()

# Petarino
# Metodi12
