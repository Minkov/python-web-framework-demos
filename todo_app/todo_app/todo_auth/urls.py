from django.urls import path

from todo_app.todo_auth.views import RegisterView, LoginView, LogoutView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
    # path('logout/', LogoutView.as_view(), name='logout user'),
)
