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
git push --set-upstream origin temp/tng
```

**pdates admin.py in your app's folder**
```
from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile)

```