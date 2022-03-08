from django.urls import path, include

from auth_demos.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView, RestrictedView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('restricted/', RestrictedView.as_view(), name='restricted'),
    # path('accounts/', include('django.contrib.auth.urls')),
)
