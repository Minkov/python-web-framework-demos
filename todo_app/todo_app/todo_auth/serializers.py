from django.contrib.auth import get_user_model
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import password_validation as validators

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')

    # Fix issue with password in plain text
    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

    def validate(self, data):
        # Invoke password validators
        user = UserModel(**data)
        password = data.get('password')
        errors = {}
        try:
            validators.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)

    # Remove password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result
