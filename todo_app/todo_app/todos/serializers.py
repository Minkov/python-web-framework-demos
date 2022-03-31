from rest_framework import serializers

from todo_app.todos.models import Todo, Category


class TodoForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title')


class TodoFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'category', 'is_done')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CategoryForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
