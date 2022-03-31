from django.urls import path

from todo_app.todos.views import TodosListAndCreateView, CategoriesListView, TodoDetailsAndUpdateView

urlpatterns = (
    path('', TodosListAndCreateView.as_view(), name='api list or create todos'),
    path('categories/', CategoriesListView.as_view(), name='api list categories'),
    path('<int:pk>/', TodoDetailsAndUpdateView.as_view(), name='api details or update todo '),
)
