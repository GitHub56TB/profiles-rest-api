from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        # Tupal using '()' to list the fields you want to use
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {  # to make password to 'write only'
            'password': {
                'write_only': True,
                # hides password as you type
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


"""Training fix ==> https://github.com/LondonAppDev/profiles-rest-api/blob/master/profiles_api/serializers.py#L34

Explanation

The default update logic for the Django REST Framework (DRF) ModelSerializer code will take whatever fields are provided (in our case: email, name, password) and pass them directly to the model.

This is fine for the email and name fields, however the password field requires some additional logic to hash the password before saving the update.

Therefore, we override the Django REST Framework's update() method to add this logic to check for the presence password in the validated_data which is passed from DRF when updating an object.

If the field exists, we will "pop" (which means assign the value and remove from the dictionary) the password from the validated data and set it using set_password() (which saves the password as a hash).

Once that's done, we use super().update() to pass the values to the existing DRF update() method, to handle updating the remaining fields.
"""

 def update(self, instance, validated_data):
      """Handle updating user account"""
       if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
