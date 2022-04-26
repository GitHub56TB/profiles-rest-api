# Build a Backend REST API with Python & Django - Beginner

This is the supplementary cheat sheet document for our course: [Build a Backend REST API with Python & Django - Beginner](https://londonapp.dev/c1)

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Build a Backend REST API with Python & Django - Beginner](#build-a-backend-rest-api-with-python--django---beginner)
  - [Git](#git)
  - [SSH Key Management](#ssh-key-management)
  - [Virtual Environments](#virtual-environments)
  - [Install required Python packages (#17)](#install-required-python-packages-17)
  - [Django Management Commands](#django-management-commands)
  - [Vagrant](#vagrant)
  - [Terminal / GitBash Commands](#terminal--gitbash-commands)

<!-- /TOC -->

## Git

Use the below Git commands in the Windows Command Prompt or macOS Terminal.

**Configure default email and name**

*Note: This only needs to be done the first time you use Git on your machine*

```
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
```

**Initialise a new Git repository**

```
git init
```

**Commit changes to Git**

```
git add .
git commit -am "Commit message"
```

**Set Git remote**

*Note: This only needs to be done once, the details are provided by GitHub after creating a new project*

```
git remote add origin <URL TO PROJECT>
git push -u origin master
```

**Push changes to GitHub**

```
git push origin
```

**Other Git Commands**

```
git remote -v

git pull origin main --rebase

git checkout -b temp/branch

git checkout main

git checkout temp/branch

git merge <BRANCH YOU WISH TO MERGE>
```

## SSH Key Management

The below commands are used to manage SSH keys on your local development machine.

**Checking for existing SSH key**

```
ls ~/.ssh/
```

**Print contents of public key**

```
cat ~/.ssh/id_rsa.pub
```

**Generate new SSH key on your local machine**

```
ssh-keygen -t rsa -b 4096 -C "EMAIL ADDRESS"
```


## Virtual Environments

The below commands are used for managing Virtual Environments using Python3-env. Use these commands when connected to your Vagrant server.

**Create new environment**

```
python3 -m venv ~/env
```

**Activate virtual environment**

```
source ~/env/bin/activate
```

**De-activate virtual environment**

```
deactivate
```

## Install required Python packages (#17)

**Create new Django project environment - Inside the '<u>requirements.txt</u>' document**

See ==> [Find, install and publish Python packages with the Python Package Index](https://pypi.org/c1)

See example below:

```
Django>=4.0.4,<4.1.0
djangorestframework==3.13.1,<3.14.0
flake8>=4.0.1,<4.1.0

```

**Install requirements from "<u>requirements.txt</u>"**

*Note: Virtual environment must be activated*

```
pip install -r requirements.txt
```

## Django Management Commands

**Create new Django project**

```
django-admin startproject profiles_project .
```

**Create new Django app**

```
python manage.py startapp profiles_api
```

**Update settings.py INSTALLED APP section**

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Add the next 3 items
    'rest_framework',
    'rest_framework.authtoken',
    'profiles_api',
]
```

**Start Django development server**

For 127.0.0.1:8000 (default)
```
python manage.py runserver
```
For 127.0.0.1:5000
```
python manage.py runserver 8000
```
For 123.4.5.6:7777
```
python manage.py runserver 123.4.5.6:7777
```

**Create database migrations file**

```
python manage.py makemigrations
```

**Run migrations**

```
python manage.py migrate
```

**Create new superuser**

```
python manage.py createsuperuser
```

## Vagrant

These commands are used for managing Vagrant using the GitBash or Terminal windows.

**Initialise Vagrant on project**

```
vagrant init ubuntu/bionic64
```

**Start Vagrant box**

```
vagrant up
```

**Connect to Vagrant box**

```
vagrant ssh
```

**Disconnect from Vagrant box**

*Note: This command is a standard linux command for ending an SSH session*

```
exit
```

**Stop Vagrant box**

```
vagrant halt
```

**Remove Vagrant box**

```
vagrant destroy
```

**Update Vagrant box image**

*Note: you must rebuild the image after updating*

```
vagrant box update
```

## Terminal / GitBash Commands

Change directory

```
cd /directory_name
```

Change to parent directory

```
cd ..
```
**Update models.py**

```
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()  # Need to create later (Class 22) - See above

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email

```
**Add to settings.py**

```
AUTH_USER_MODEL = 'profiles_api.UserProfile'

```

**Create database migrations file**

```
python manage.py makemigrations profiles_api
```

**Run migrations**

```
python manage.py migrate

git push --set-upstream origin temp/tng
```

**Push updates to GitHub**

```
git status
git add . 
git commit -am "Updated Readme to show remote commit command for a branch"
git push --set-upstream origin temp/tng
```

**Update admin.py in your app's folder**
```
from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile)

```
**Push updates to GitHub**

```
git status
git add . 
git commit -am "Enable Django admin for user profile model"
git push
```
**APIView**
**Update views.py in your app's folder**
```
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # Need to return a disctionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
```

**APIView**
**Update views.py in your app's folder**
- Create a "urls.py" under profiles_api folder
- Update the **Project's** urls.py with the following
```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]

```

**APIView**
**Update urls.py in your app's folder (profiles_api)**
```
from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]

```

**APIView**
**python manage.py runserver**
See results below:
```

Django REST framework (http://127.0.0.1:8000/api/hello-view/)


Hello Api
Test API View

GET /api/hello-view/

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "message": "Hello!",
    "an_apiview": [
        "Uses HTTP methods as functions (get, post, patch, put, delete)",
        "Is similar to a traditional Django View",
        "Gives you the most control over your logic",
        "Is mapped manually to URLs"
    ]
}
```

**Push updates to GitHub**

```
git status
git add . 
git commit -am "Added HelloApiView and updated Readme"
git push
```

**APIView**
**Create a "serializers.py" under profiles_api folder and update**
```
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

```

**APIView**
**Update profiles_api/views.py**

```
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer  # Get functiion from serializer.py (Key item !!!)

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # Must return a dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})  # Must return a dictionary
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating/replacing an object"""

        return Response({'method': 'PUT'})  # Must return a dictionary

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})  # Must return a dictionary

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})  # Must return a dictionary


```
**Push updates to GitHub**

```
git status
git add . 
git commit -am "Added POST, PATCH, PUT, DELETE methods to APIView"
git push
```
**Viewsets**
**Update/Register/Add Routers profiles_api/urls.py**

```
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet,
                basename='hello-viewset')  # Training Class 40 - https://www.django-rest-framework.org/api-guide/viewsets/ (use basename versus base_name; 'r' is optional)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]

```
**Viewsets**
**Update profiles_api/views.py**

```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer  # Get functiion from serializer.py (Key item !!!)

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # Must return a dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})  # Must return a dictionary
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating/replacing an object"""

        return Response({'method': 'PUT'})  # Must return a dictionary

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})  # Must return a dictionary

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})  # Must return a dictionary


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer  # Added Class #42

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

```
**Push updates to GitHub**

```
git status
git add . 
git commit -am "Added POST, PATCH, PUT, DELETE methods to Viewset"
git push
```
**API Viewsets Profiles Project**
**Update profiles_api/views.py**

```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer  # Get functiion from serializer.py (Key item !!!)

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        # Must return a dictionary
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})  # Must return a dictionary
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating/replacing an object"""

        return Response({'method': 'PUT'})  # Must return a dictionary

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})  # Must return a dictionary

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})  # Must return a dictionary


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer  # Added Class #42

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

```
**API Viewsets Profiles Project**
**Update profiles_api/serializers.py**

```
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



```
**API Viewsets Profiles Project**
**Update profiles_api/urls.py**

```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet,
                basename='hello-viewset')  # Training Class 40 - https://www.django-rest-framework.org/api-guide/viewsets/ (use basename versus base_name; 'r' is optional)
router.register(r'profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]

```
**API Viewsets Profiles Project**
**Update profiles_api/permissions.py**
```
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id  # Return True if user is different

```
**API Viewsets Profiles Project - SHORT**
**Update profiles_api/views.py**
```
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
...

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    ...
    # add a comma to make a tuple
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
```
**API Viewsets Profiles Project - SHORT (Search)**
**Update profiles_api/views.py**
```
from rest_framework import filters

...

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    ...
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
```
**Push updates to GitHub**
```
git add . 
git commit -am "Added Profiles Viewset with Search"
git push
```
**API Viewsets Profiles Project**
**Update profiles_api/views.py**