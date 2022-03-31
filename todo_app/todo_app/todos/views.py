from django.core import exceptions
from rest_framework import generics as api_views, permissions

from todo_app.todos.models import Todo, Category
from todo_app.todos.serializers import TodoFullSerializer, TodoForListSerializer, CategoryForListSerializer


class TodosListAndCreateView(api_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )
    query_filter_names = ('category',)

    list_serializer_class = TodoForListSerializer
    create_serializer_class = TodoFullSerializer

    def __apply_query_filters(self, queryset):
        filter_options = {}
        for filter_name in self.query_filter_names:
            value = self.request.query_params.get(filter_name, None)
            if value:
                filter_options[f'{filter_name}_id'] = value

        return queryset.filter(**filter_options)

    # /api/todos/?category=2
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(user=self.request.user)

        queryset = self.__apply_query_filters(queryset)

        return queryset

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return self.create_serializer_class
        return self.list_serializer_class


class TodoDetailsAndUpdateView(api_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoFullSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        the_object = super().get_object()
        if the_object.user != self.request.user:
            raise exceptions.PermissionDenied
        return the_object


class CategoriesListView(api_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(todo__user=self.request.user)
    #     return queryset
