import sys
import os
from pathlib import Path
from distutils.file_util import move_file

with open('django-creator.py', 'r') as file:
    content = file.read()
    content.replace('{path_to_python}', sys.executable)

os.makedirs('bin', exist_ok=True)
with open('bin/django-creator', 'w') as file:
    file.write(content)

# Add bin folder to path
os.environ['PATH'] += os.pathsep + str(Path('bin').resolve())


# Save the content into python executable directory
# with open(os.path.join('bin', 'django-creator.py'), 'w') as file:
#     file.write(content)

