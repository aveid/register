from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class IndexPageView(TemplateView):
    template_name = 'index.html'


class UserCabinetView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'cabinet.html'

    def get_object(self, queryset=None):
        # if self.request.user.has_perm('can_get_name'):
        return User.objects.get(username=self.request.user.username)






