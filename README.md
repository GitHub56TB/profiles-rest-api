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
