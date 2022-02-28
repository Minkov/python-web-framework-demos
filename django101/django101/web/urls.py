from django.urls import path

from django101.web.views import index, IndexView, IndexTemplateView, TodosListView, TodoDetailsView, TodoCreateView

urlpatterns = (
    path('', index, name='index func-based'),
    path('cbv/', IndexView.as_view(), name='index class-based'),
    path('cbv-template/', IndexTemplateView.as_view(), name='index class-based (template)'),
    path('todos/', TodosListView.as_view(), name='todos list'),
    path('todos/<int:pk>/', TodoDetailsView.as_view(), name='todo details'),
    path('todos/create/', TodoCreateView.as_view(), name='create todo'),
)
