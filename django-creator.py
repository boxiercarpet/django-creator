#!{path_to_python}

import os.path
from os import getcwd
from subprocess import DEVNULL
from venv import EnvBuilder
import subprocess

art = """
=======================================================
\033[94m ▗▄▄▖▗▄▄▖ ▗▄▄▄▖ ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖\033[0m▗▖ ▗▖▗▖ ▗▖▗▄▄▖ 
\033[94m▐▌   ▐▌ ▐▌▐▌   ▐▌ ▐▌ █    █  ▐▌  ▐▌▐▌   \033[0m▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌
\033[94m▐▌   ▐▛▀▚▖▐▛▀▀▘▐▛▀▜▌ █    █  ▐▌  ▐▌▐▛▀▀▘\033[0m▐▛▀▜▌▐▌ ▐▌▐▛▀▚▖
\033[94m▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌ █  ▗▄█▄▖ ▝▚▞▘ ▐▙▄▄▖\033[0m▐▌ ▐▌▝▚▄▞▘▐▙▄▞▘
\033[0m=================== \033[1mDJANGO CREATOR\033[0m ====================
"""
print(art)

project_name = input("Give your project a name: ")

print("Creating virtual environment...")
dir = getcwd()
env = EnvBuilder(with_pip=True)
env.create(os.path.join(dir, '.venv'))
env_context = env.ensure_directories(os.path.join(dir, '.venv'))

def run_command(command):
    subprocess.run(command, env={"PATH": env_context.bin_path, "DJANGO_SUPERUSER_PASSWORD": "admin"}, stdout=DEVNULL)

print("Installing Django...")
run_command( ['pip', 'install', 'django'])

print("Creating Django project...")
run_command( ['django-admin', 'startproject', project_name+"_project", '.'])

print("Creating Django app...")
run_command( ['python', 'manage.py', 'startapp', project_name])

print("Creating Django migrations...")
run_command( ['python', 'manage.py', 'makemigrations'])
run_command( ['python', 'manage.py', 'migrate'])

print("Creating Django superuser...")
run_command( ['python', 'manage.py', 'createsuperuser', '--username=admin', '--email=admin@example.com', '--noinput'])

print("Preparing Django files...")
with open(os.path.join(dir, project_name, 'urls.py'), 'w') as f:
    f.write(f"""from django.urls import path
from . import views

urlpatterns = [
    # Add your urls here
]
""")

with open(os.path.join(dir, project_name + "_project", 'urls.py')) as f:
    urls_content = f.read()

with open(os.path.join(dir, project_name + "_project", 'urls.py'), 'w') as f:
    f.write(urls_content.replace("import path", "import path, include").replace("urlpatterns = [", f"urlpatterns = [\n    path('', include('{project_name}.urls')),"))

print("Django project created successfully!\n")
print("To run the server, execute: python manage.py runserver")
print("Super user created with username: \033[94madmin\033[0m and password: \033[94madmin\033[0m")