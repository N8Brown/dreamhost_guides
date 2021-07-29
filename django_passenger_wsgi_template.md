# DreamHost Guide: The Django `passenger_wsgi.py` Template

DreamHost allows users to host Python-backed Django projects on their servers, but they require a special file, `passenger_wsgi.py`, in order to work properly. This guide will explain in detail how to use the accompanying `passenger_wsgi.py` template file and configure it for your project. This process assumes that a virtual environment has been set up, Django has been installed, and all Django project files have either been cloned from GitHub or uploaded via DreamHost's WebFTP tool or a 3rd party option such as FileZilla.

If the previously mentioned steps have not been completed, please stop and complete those first before proceeding.

## Passenger

DreamHost uses Passenger to handle HTTP requests for projects based in Ruby, Python, or Node.js. So what is Passenger? According to the [Passenger Overview](https://help.dreamhost.com/hc/en-us/articles/215769578-Passenger-overview) on the DreamHost Knowledge Base, *"Passenger is an open-source web and application server that greatly simplifies the deployment of Ruby, Python, and Node.js applications."* 

The `passenger_wsgi.py` file is what allows the Passenger server to connect to and serve a Django project, and is therefore a crucial part the deployment of a Django-based website or application.

## Template

The accompanying template is fairly straightforward, however, there are five sections that must be configured in order to work properly. Anywhere in the code that contains text between two angled brackets, `<example>`, represents a section of code that needs to be configured. These sections are indicated by comments at the end of a line of code referencing their corresponding sections in this guide. Download the template and open it in a text editor to configure.  

![passenger_wsgi.py file](/img/passenger_wsgi.jpg)

### Section 1

A Python interpreter needs to be defined in order for the server to know which instance of Python to use. To do this, simply replace `<python_interpreter_path_here>` with the path to the Python instance in the virtual environment 

```py
INTERP = "<python_interpreter_path_here>"  #See Guide: Template - Section 1
```

Example:
```py
INTERP = "home/user/example.com/env/bin/python3"
```

*(NOTE: You can SSH into your DreamHost server from a terminal, navigate to the* `bin` *directory of the virtual environment, and use the* `pwd` *command get the full path. Copy and paste as a string into the template and then add python3 to the end)*

### Section 2

Add the Django project by replacing `<django_project_name_here>` with the name of the Django project folder

```py
sys.path.append(cwd + '/<django_project_name_here>')  #See Guide: Template - Section 2
```

Example:
```py
sys.path.append(cwd + '/djangoproject')
```

If the project root directory (the folder containing the Django project folder, app folders and `manage.py`) name is different from the main project directory (the folder containing `settings.py`), then it is the project root directory that should be referenced.

```bash
|---environment_name
|---project_root        <---- (Use this folder name)
    |---app_folder
    |---main_project
        |---__init__.py
        |---asgi.py
        |---settings.py
        |---urls.py
        |---wsgi.py
    |---manage.py
```

### Section 3
Add the virtual environment bin location by replacing `<virtual_environment_name_here>` with the name of the virtual environment directory

```py
sys.path.insert(0,cwd+'/<virtual_environment_name_here>/bin') #See Guide: Template - Section 3
```

Example:
```py
sys.path.insert(0,cwd+'/<env/bin')
```

### Section 4
Add the virtual environment site packages by replacing `<virtual_environment_name_here>` with the name of the virtual environment directory and `<python_version_directory_name_here>` with the name of the Python version directory.

```py
sys.path.insert(0,cwd+'/<virtual_environment_name_here>/lib/<python_version_directory_name_here>/site-packages') #See Guide: Template - Section 4
```

Example:
```py
sys.path.insert(0,cwd+'/env/lib/python3.9/site-packages') 
```

### Section 5

Set Django settings module as an `os.environ` variable by changing `<django_project_name_here>` to the name of the main project directory (the folder containing `settings.py`)

```py
os.environ['DJANGO_SETTINGS_MODULE'] = "<django_project_name_here>.settings"
```

Example:
```py
os.environ['DJANGO_SETTINGS_MODULE'] = "djangoproject.settings"
```

```bash
|---environment_name
|---project_root
    |---app_folder        
    |---main_project    <---- (Use this folder name)
        |---__init__.py
        |---asgi.py
        |---settings.py
        |---urls.py
        |---wsgi.py
    |---manage.py
```


### Finished Template

Once all sections have been configured, the template file should look something like this:

```py
import sys, os

INTERP = "home/user/example.com/env/bin/python3" 
 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/djangoproject')

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python3.9/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "djangoproject.settings" 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Save the file and follow the next steps to upload it to the proper location on the DreamHost server.

*(NOTE: Do NOT change the name of the file)*

## Final Steps

With the `passenger_wsgi.py` template configured, it now needs to be uploaded to the correct location.

The base path to a DreamHost website should look something like this:

```bash
/home/user/example.com/
```

Within that location should be a basic file structure that contains the virtual environment directory, the Django project root directory, and a directory called public:

```bash
|---environment_name
|---project_root
    |---app_folder        
    |---main_project
        |---__init__.py
        |---asgi.py
        |---settings.py
        |---urls.py
        |---wsgi.py
    |---manage.py
|---public
```

*(NOTE: If you see an additional directory named* `__pycache__` *that is normal and you can leave it)*

It is in the website's base path directory that the `passenger_wsgi.py` file should be placed. 

```bash
|---environment_name
|---project_root
    |---app_folder        
    |---main_project
        |---__init__.py
        |---asgi.py
        |---settings.py
        |---urls.py
        |---wsgi.py
    |---manage.py
|---public
|---passenger_wsgi.py
```

*(NOTE: You can use DreamHost's WebFTP tool, or a 3rd part tool such as FileZilla to upload the* `passenger_wsgi.py` *file to the server)*

Lastly, in order get Passenger to register the `passenger_wsgi.py` file, make sure that you are in the website's base path directory and run the following commands from a terminal:

```bash
mkdir tmp
```

```bash
touch tmp/restart.txt
```

The first command creates a temporary directory, and the second command adds a file called `restart.txt` to the new temporary directory. According to the [DreamHost Knowledge Base](https://help.dreamhost.com/hc/en-us/articles/360002341572-Creating-a-Django-project), this notifies Passenger of a change. Any future changes should be accompanied by running the second command `touch tmp/restart.txt` from the website base path directory.