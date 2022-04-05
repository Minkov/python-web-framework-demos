from django.urls import path

from exceptions_demos.web.views import raises_exception_view, MyView

urlpatterns = (
    path('exception/', raises_exception_view),
    path('login-required/', MyView.as_view(), )
)
