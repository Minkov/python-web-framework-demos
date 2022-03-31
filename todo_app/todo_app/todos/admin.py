from django.contrib import admin

from todo_app.todos.models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'is_done')

    def username(self, obj):
        return obj.user.username


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
