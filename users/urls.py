from django.urls import path

from users.views import CreateUserView, IndexPageView, UserCabinetView

app_name = 'users'

urlpatterns = [
    path('accounts/register/', CreateUserView.as_view(), name='register'),
    path('', IndexPageView.as_view(), name='index'),
    path('accounts/cabinet/', UserCabinetView.as_view(), name='cabinet'),
]